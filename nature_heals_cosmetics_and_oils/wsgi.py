"""
WSGI config for nature_heals_cosmetics_and_oils project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nature_heals_cosmetics_and_oils.settings')

application = get_wsgi_application()
