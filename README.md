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
| [home-assistant/core](https://github.com/home-assistant/core) | LIKELY | 1465 | 1057 | 92% | 5 h |
| [python/cpython](https://github.com/python/cpython) | LIKELY | 1455 | 957 | 89% | 1 h |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | LIKELY | 1142 | 749 | 88% | 8 h |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | LIKELY | 1783 | 939 | 86% | 4 h |
| [encode/httpx](https://github.com/encode/httpx) | LIKELY | 33 | 5 | 83% | 1 h |
| [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | MIXED | 297 | 185 | 70% | 2 days |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | MIXED | 1637 | 322 | 68% | 22 h |
| [astral-sh/ruff](https://github.com/astral-sh/ruff) | MIXED | 714 | 368 | 63% | 18 h |
| [numpy/numpy](https://github.com/numpy/numpy) | MIXED | 358 | 160 | 61% | 35 h |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | MIXED | 627 | 228 | 51% | 30 h |
| [huggingface/transformers](https://github.com/huggingface/transformers) | MIXED | 987 | 361 | 51% | 2 days |
| [django/django](https://github.com/django/django) | UNLIKELY | 412 | 98 | 35% | 3 days |
| [pydantic/pydantic](https://github.com/pydantic/pydantic) | UNLIKELY | 328 | 94 | 34% | 5 h |
| [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | UNLIKELY | 328 | 75 | 33% | 28 h |
| [pytest-dev/pytest](https://github.com/pytest-dev/pytest) | UNLIKELY | 292 | 29 | 19% | 8 days |
| [pallets/flask](https://github.com/pallets/flask) | UNLIKELY | 13 | 0 | 0% | n/a |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | UNLIKELY | 131 | 0 | 0% | n/a |
| [psf/requests](https://github.com/psf/requests) | NO DATA | 0 | 0 | n/a | n/a |

Snapshot of 2026-11-26, pull requests from the last 90 days.
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
