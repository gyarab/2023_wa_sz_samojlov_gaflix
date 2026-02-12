"""
WSGI config for gaflix project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Allow Python to find the gaflix module
sys.path.append(str(BASE_DIR))

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gaflix.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Safe DB initialization
def ensure_db():
    from django.db import connection
    from django.core.management import call_command

    try:
        connection.ensure_connection()
    except:
        call_command("migrate", interactive=False)

ensure_db()

app = application
