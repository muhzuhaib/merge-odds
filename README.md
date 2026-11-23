# merge-odds

How do popular Python projects treat pull requests from people outside their team?

Every weekday a scheduled job runs [willitmerge](https://github.com/muhzuhaib/willitmerge) over the
projects in [`repos.txt`](repos.txt), looking at the pull requests of the last 90 days, and keeps the
result in [`data/`](data/), one file per day. Read over time, the files show which projects stay
open to newcomers and which slow down.

## Latest snapshot

<!-- latest:start -->
| Project | Verdict | Outside PRs | Merged | Merge rate | Median time to merge |
|---|---|---:|---:|---:|---:|
| [home-assistant/core](https://github.com/home-assistant/core) | LIKELY | 1492 | 991 | 91% | 4 h |
| [python/cpython](https://github.com/python/cpython) | LIKELY | 1473 | 989 | 90% | 1 h |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | LIKELY | 1125 | 714 | 88% | 8 h |
| [encode/httpx](https://github.com/encode/httpx) | LIKELY | 21 | 4 | 80% | 1 h |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | LIKELY | 1771 | 851 | 79% | 3 h |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | MIXED | 1623 | 339 | 69% | 25 h |
| [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | MIXED | 300 | 173 | 69% | 48 h |
| [numpy/numpy](https://github.com/numpy/numpy) | MIXED | 353 | 161 | 62% | 35 h |
| [astral-sh/ruff](https://github.com/astral-sh/ruff) | MIXED | 736 | 367 | 61% | 19 h |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | MIXED | 626 | 231 | 50% | 29 h |
| [huggingface/transformers](https://github.com/huggingface/transformers) | MIXED | 987 | 360 | 49% | 3 days |
| [pydantic/pydantic](https://github.com/pydantic/pydantic) | UNLIKELY | 333 | 96 | 34% | 4 h |
| [django/django](https://github.com/django/django) | UNLIKELY | 425 | 94 | 33% | 3 days |
| [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | UNLIKELY | 319 | 72 | 33% | 28 h |
| [pytest-dev/pytest](https://github.com/pytest-dev/pytest) | UNLIKELY | 290 | 30 | 19% | 8 days |
| [pallets/flask](https://github.com/pallets/flask) | UNLIKELY | 14 | 0 | 0% | n/a |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | UNLIKELY | 133 | 0 | 0% | n/a |
| [psf/requests](https://github.com/psf/requests) | NO DATA | 0 | 0 | n/a | n/a |

Snapshot of 2026-11-23, pull requests from the last 90 days.
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
