# -*- coding: utf-8 -*-
from tempfile import mkdtemp


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

FILE_UPLOAD_TEMP_DIR = mkdtemp()

MIDDLEWARE_CLASSES = [
    'django.middleware.csrf.CsrfViewMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]
