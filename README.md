# merge-odds

How do popular Python projects treat pull requests from people outside their team?

Every weekday a scheduled job runs [willitmerge](https://github.com/muhzuhaib/willitmerge) over the
projects in [`repos.txt`](repos.txt), looking at the pull requests of the last 90 days, and keeps the
result in [`data/`](data/), one file per day. Read over time, the files show which projects stay
open to newcomers and which slow down.

## Latest snapshot

<!-- latest:start -->
The first snapshot appears after the first scheduled run.
<!-- latest:end -->

**Outside PRs** are pull requests from authors who are not members, owners or collaborators.
**Merge rate** is merged outside PRs divided by outside PRs that were merged or closed.
**Verdict** is willitmerge's reading of that evidence; NO DATA means too few outside PRs to say.

## Run it yourself

```bash
pip install willitmerge pytest
python -m pytest -q
GITHUB_TOKEN=<your token> python snapshot.py
```

To follow another project, add one line to `repos.txt`.

## License

MIT
