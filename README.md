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
| [home-assistant/core](https://github.com/home-assistant/core) | LIKELY | 1481 | 1024 | 92% | 4 h |
| [python/cpython](https://github.com/python/cpython) | LIKELY | 1469 | 978 | 90% | 2 h |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | LIKELY | 1134 | 740 | 88% | 10 h |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | LIKELY | 1782 | 890 | 83% | 3 h |
| [encode/httpx](https://github.com/encode/httpx) | LIKELY | 25 | 4 | 80% | 1 h |
| [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | MIXED | 300 | 184 | 69% | 2 days |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | MIXED | 1624 | 326 | 69% | 25 h |
| [astral-sh/ruff](https://github.com/astral-sh/ruff) | MIXED | 731 | 375 | 63% | 19 h |
| [numpy/numpy](https://github.com/numpy/numpy) | MIXED | 354 | 158 | 61% | 35 h |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | MIXED | 631 | 230 | 50% | 30 h |
| [huggingface/transformers](https://github.com/huggingface/transformers) | MIXED | 978 | 361 | 50% | 3 days |
| [pydantic/pydantic](https://github.com/pydantic/pydantic) | UNLIKELY | 333 | 97 | 34% | 7 h |
| [django/django](https://github.com/django/django) | UNLIKELY | 429 | 97 | 34% | 3 days |
| [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | UNLIKELY | 324 | 73 | 32% | 28 h |
| [pytest-dev/pytest](https://github.com/pytest-dev/pytest) | UNLIKELY | 291 | 29 | 19% | 8 days |
| [pallets/flask](https://github.com/pallets/flask) | UNLIKELY | 14 | 0 | 0% | n/a |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | UNLIKELY | 135 | 0 | 0% | n/a |
| [psf/requests](https://github.com/psf/requests) | NO DATA | 0 | 0 | n/a | n/a |

Snapshot of 2026-11-24, pull requests from the last 90 days.
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
