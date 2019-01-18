"""
Django development settings for kalender project.
"""

from kalender.settings.common import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']
INTERNAL_IPS = ['127.0.0.1', '10.49.20.40', '10.49.20.50']

INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
