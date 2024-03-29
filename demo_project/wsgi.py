"""
WSGI config for demo_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django_forest import init_forest
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_project.settings')

init_forest()
application = get_wsgi_application()
