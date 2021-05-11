from resume.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
	'128.199.144.194',
    'api.swongdev.com',
	'localhost',
]

CORS_ALLOWED_ORIGINS = [
    "https://swongdev.com/",
    "https://www.swongdev.com/",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': 'localhost',
        'PORT': '',
    }
}
