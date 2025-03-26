"""
ASGI config for ecommerce project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Set the default settings module for the 'asgi' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

# Get the ASGI application for the project
application = get_asgi_application()
