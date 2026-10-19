# TODO List

A simple task manager built with Django. Add tasks with a title and description, then update or delete them from the list.

## Features

- Create, view, edit, and delete tasks
- Store a task title, optional description, and creation timestamp
- Responsive interface with custom CSS
- Django admin interface
- SQLite for local development; database URL support for deployment

## Tech Stack

- Python 3.13
- Django 6.1
- WhiteNoise for static files
- SQLite locally, configurable through `DATABASE_URL`
- Vercel deployment configuration

## Run Locally

Requirements: Python 3.13 or a compatible Python version.

From the repository root:

```powershell
cd todo
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser. To create an admin account, run:

```powershell
python manage.py createsuperuser
```

Then visit <http://127.0.0.1:8000/admin/>.

## Deploy to Vercel

1. Import this GitHub repository into Vercel.
2. Set the Vercel project **Root Directory** to `todo`.
3. Deploy using the included `vercel.json` configuration.

The project accepts a `DATABASE_URL` environment variable. For hosted use, configure it with a managed PostgreSQL database; SQLite files on serverless deployments should not be treated as persistent storage.

Before using this app publicly, configure a private `SECRET_KEY` and turn `DEBUG` off in Django settings.

## Project Layout

```text
todo/
├── list/             # Task model, views, forms, templates, and migrations
├── static/           # Stylesheet
├── todo/             # Django project settings and WSGI entry point
├── manage.py
├── requirements.txt
└── vercel.json
```
