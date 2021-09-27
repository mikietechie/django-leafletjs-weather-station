'''
Copyrights 2021
Work Done By Mike Zinyoni https://github.com/mikietechie
mzinyoni7@gmail.com (Do not spam please)
(Open to work)
'''

"""
ASGI config for weather project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')

application = get_asgi_application()
