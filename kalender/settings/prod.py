"""
Django development settings for kalender project.
"""

from kalender.settings.common import *

DEBUG = False

ALLOWED_HOSTS = [
    'kro-lev-srv-608.kronosww.com',
    'localhost',
    '127.0.0.1',
    '127.0.0.1:8765',
]

STATIC_URL = 'https://kro-lev-srv-608.kronosww.com:8443/kalender/'
STATIC_ROOT = '/var/www/static/kalender/'
