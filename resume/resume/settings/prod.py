from resume.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
	'128.199.144.194',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}