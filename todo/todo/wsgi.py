"""
WSGI config for todo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

# application = get_wsgi_application()



import os
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

application = get_wsgi_application()

# Vercel starts with a fresh filesystem/database, so apply pending migrations
# before the first request accesses application tables.
call_command('migrate', interactive=False, verbosity=0)

# Vercel requires 'app' variable exposure for WSGI
app = application
