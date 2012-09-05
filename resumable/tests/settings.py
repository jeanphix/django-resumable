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
    'django.contrib.staticfiles',
    'resumable',
    'resumable.tests.app',
]

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'secret'

ROOT_URLCONF = 'resumable.tests.app'

FILE_UPLOAD_TEMP_DIR = '%s/resumable-test' % gettempdir()
