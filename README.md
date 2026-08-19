# leetcode-tracker

Django backend for tracking daily LeetCode progress: which problems you solved,
in what language, how long each took, and where the gaps are.

## Data model

| Model | Holds |
|---|---|
| `problem` | name, difficulty, acceptance rate, current status |
| `solution` | the attempt: language, notes, date solved, time spent |
| `status` | the states a problem can be in |

## Status

**This is a skeleton, not a finished project.** The models and the Django admin
work — you can record and browse progress through `/admin/`. There is no API
yet: `graphene` is listed in `requirements.txt` and `graphqlqueries.py` is still
empty, so nothing is exposed over GraphQL or REST.

## Running it

```bash
pip install -r requirements.txt
cd tracker
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver     # admin at /admin/
```

## Licence
MIT
