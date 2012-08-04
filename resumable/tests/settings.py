# -*- coding: utf-8 -*-
from tempfile import gettempdir


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'resumable.db',
    },
}

INSTALLED_APPS = [
    'resumable',
    'resumable.tests.app',
]

STATIC_URL = '/static/'

SECRET_KEY = 'secret'

ROOT_URLCONF = 'resumable.tests.app'

CHUNKS_ROOT = '%s/resumable-test' % gettempdir()
