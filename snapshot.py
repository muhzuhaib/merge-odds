"""Take today's snapshot: run willitmerge over repos.txt, save data/<date>.json, refresh README.md.

Run once a weekday by .github/workflows/snapshot.yml. A second run on the same UTC day finds the
file already there and changes nothing, so the workflow can be scheduled twice for safety.
"""

from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
README = ROOT / "README.md"
REPOS = ROOT / "repos.txt"
DAYS = 90
START = "<!-- latest:start -->"
END = "<!-- latest:end -->"


def read_repos(text: str) -> list[str]:
    """One OWNER/REPO per line; blank lines and # comments are ignored."""
    repos = []
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            repos.append(line)
    return repos


def percent(rate: float | None) -> str:
    return "n/a" if rate is None else f"{rate * 100:.0f}%"


def hours(value: float | None) -> str:
    if value is None:
        return "n/a"
    if value < 48:
        return f"{value:.0f} h"
    return f"{value / 24:.0f} days"


def render_table(snapshot: dict) -> str:
    rows = [
        "| Project | Verdict | Outside PRs | Merged | Merge rate | Median time to merge |",
        "|---|---|---:|---:|---:|---:|",
    ]
    results = sorted(snapshot["results"], key=lambda r: (r["merge_rate"] is None, -(r["merge_rate"] or 0)))
    for r in results:
        rows.append(
            f"| [{r['repo']}](https://github.com/{r['repo']}) | {r['verdict']} | {r['outsider_pulls']} "
            f"| {r['merged']} | {percent(r['merge_rate'])} | {hours(r['median_hours'])} |"
        )
    note = f"Snapshot of {snapshot['date']}, pull requests from the last {snapshot['window_days']} days."
    if snapshot["errors"]:
        note += f" Not measured this time: {len(snapshot['errors'])} (details in the data file)."
    return "\n".join(rows) + "\n\n" + note


def replace_block(readme: str, block: str) -> str:
    head, sep, rest = readme.partition(START)
    if not sep or END not in rest:
        raise SystemExit("README.md is missing the latest:start / latest:end markers")
    return f"{head}{START}\n{block}\n{END}{rest.split(END, 1)[1]}"


def measure(repos: list[str]) -> dict:
    proc = subprocess.run(
        [sys.executable, "-m", "willitmerge", *repos, "--days", str(DAYS), "--json"],
        capture_output=True,
        text=True,
        timeout=1500,
    )
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        raise SystemExit(f"willitmerge gave no JSON (exit {proc.returncode}): {proc.stderr.strip()[:500]}")


def main() -> int:
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    out = DATA / f"{today}.json"
    if out.exists():
        print(f"{out.name} already exists; nothing to do")
        return 0
    report = measure(read_repos(REPOS.read_text(encoding="utf-8")))
    if not report.get("results"):
        print(f"no repository could be measured: {report.get('errors')}")
        return 1
    snapshot = {"date": today, "window_days": DAYS, **report}
    DATA.mkdir(exist_ok=True)
    out.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    README.write_text(replace_block(README.read_text(encoding="utf-8"), render_table(snapshot)), encoding="utf-8")
    print(f"wrote {out.name}: {len(snapshot['results'])} measured, {len(snapshot['errors'])} not")
    return 0


if __name__ == "__main__":
    sys.exit(main())
