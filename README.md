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
| [home-assistant/core](https://github.com/home-assistant/core) | LIKELY | 1478 | 1066 | 92% | 5 h |
| [python/cpython](https://github.com/python/cpython) | LIKELY | 1467 | 974 | 90% | 2 h |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | LIKELY | 1127 | 741 | 88% | 10 h |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | LIKELY | 1777 | 931 | 85% | 3 h |
| [encode/httpx](https://github.com/encode/httpx) | LIKELY | 26 | 4 | 80% | 1 h |
| [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | MIXED | 297 | 183 | 69% | 2 days |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | MIXED | 1632 | 320 | 68% | 24 h |
| [astral-sh/ruff](https://github.com/astral-sh/ruff) | MIXED | 719 | 372 | 63% | 18 h |
| [numpy/numpy](https://github.com/numpy/numpy) | MIXED | 355 | 158 | 61% | 35 h |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | MIXED | 626 | 229 | 51% | 29 h |
| [huggingface/transformers](https://github.com/huggingface/transformers) | MIXED | 982 | 361 | 50% | 3 days |
| [pydantic/pydantic](https://github.com/pydantic/pydantic) | UNLIKELY | 332 | 96 | 34% | 6 h |
| [django/django](https://github.com/django/django) | UNLIKELY | 418 | 95 | 34% | 3 days |
| [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | UNLIKELY | 330 | 74 | 33% | 28 h |
| [pytest-dev/pytest](https://github.com/pytest-dev/pytest) | UNLIKELY | 291 | 29 | 19% | 8 days |
| [pallets/flask](https://github.com/pallets/flask) | UNLIKELY | 14 | 0 | 0% | n/a |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | UNLIKELY | 133 | 0 | 0% | n/a |
| [psf/requests](https://github.com/psf/requests) | NO DATA | 0 | 0 | n/a | n/a |

Snapshot of 2026-11-25, pull requests from the last 90 days.
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
