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
from django.core.management import call_command

try:
    call_command("migrate", interactive=False)
except Exception as e:
    print("Migration error:", e)

try:
    call_command("loaddata", "app/fixtures/data.json")
except Exception as e:
    print("Fixture error:", e)


application = get_wsgi_application()

app = application
