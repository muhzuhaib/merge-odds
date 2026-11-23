import pytest

import snapshot as s


def result(repo, rate, merged=1, median=5.0):
    return {"repo": repo, "verdict": "LIKELY", "outsider_pulls": 4, "merged": merged,
            "merge_rate": rate, "median_hours": median}


def test_repos_file_skips_blanks_and_comments():
    assert s.read_repos("a/b\n\n# note\nc/d  # why\n") == ["a/b", "c/d"]


def test_table_sorts_by_merge_rate_and_puts_unknown_last():
    snap = {"date": "2026-11-23", "window_days": 90, "errors": [],
            "results": [result("x/none", None, 0, None), result("x/low", 0.2), result("x/high", 0.9)]}
    lines = s.render_table(snap).splitlines()
    assert [ln.split("]")[0][3:] for ln in lines[2:5]] == ["x/high", "x/low", "x/none"]
    assert "| n/a | n/a |" in lines[4]


def test_errors_are_counted_in_the_note():
    snap = {"date": "2026-11-23", "window_days": 90, "errors": ["a/b: HTTP 404"], "results": [result("x/y", 0.5)]}
    assert "Not measured this time: 1" in s.render_table(snap)


def test_hours_switch_to_days_after_two_days():
    assert s.hours(30) == "30 h"
    assert s.hours(72) == "3 days"


def test_block_between_markers_is_replaced_and_the_rest_kept():
    readme = f"top\n{s.START}\nold\n{s.END}\nbottom\n"
    assert s.replace_block(readme, "new") == f"top\n{s.START}\nnew\n{s.END}\nbottom\n"


def test_missing_markers_stop_the_run():
    with pytest.raises(SystemExit):
        s.replace_block("no markers here", "new")


def test_a_second_run_on_the_same_day_changes_nothing(tmp_path, monkeypatch):
    monkeypatch.setattr(s, "DATA", tmp_path)
    today = s.dt.datetime.now(s.dt.timezone.utc).date().isoformat()
    (tmp_path / f"{today}.json").write_text("{}")
    monkeypatch.setattr(s, "measure", lambda repos: pytest.fail("must not measure again"))
    assert s.main() == 0
