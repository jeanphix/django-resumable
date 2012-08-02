DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'resumable.db',
    },
}

INSTALLED_APPS = [
    'resumable',
]

STATIC_URL = '/static/'

SECRET_KEY = 'secret'
