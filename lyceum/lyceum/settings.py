import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _
import environ

import lyceum.utils

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, './../.env'), overwrite=False)
SECRET_KEY = env.str('DJANGO_SECRET_KEY', default='secret')

REQUESTS_COUNT_BEFORE_REVERSE = env.int(
    'DJANGO_REQUESTS_COUNT_BEFORE_REVERSE',
    default=10,
)

DEBUG = lyceum.utils.str_to_bool(env.str('DJANGO_DEBUG', default='False'))
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['*'])

ALLOW_REVERSE = lyceum.utils.str_to_bool(
    env.str('DJANGO_ALLOW_REVERSE', default='True'),
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'about.apps.AboutConfig',
    'catalog.apps.CatalogConfig',
    'core.apps.CoreConfig',
    'homepage.apps.HomepageConfig',
    'download.apps.DownloadConfig',
    'feedback.apps.FeedbackConfig',
    'sorl.thumbnail',
    'django_cleanup.apps.CleanupConfig',
    'django_ckeditor_5',
] + (['debug_toolbar'] if DEBUG else [])

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'lyceum.middleware.ReverseRussianMiddleware',
    'django.middleware.locale.LocaleMiddleware',
] + (['debug_toolbar.middleware.DebugToolbarMiddleware'] if DEBUG else [])

INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'lyceum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lyceum.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.NumericPasswordValidator'
        ),
    },
]


LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
LANGUAGES = [
    ('ru', _('Русский')),
    ('en', _('English')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static_dev',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

EMAIL_SACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': {
            'items': [
                'heading',
                '|',
                'bold',
                'italic',
                'link',
                'bulletedList',
                'numberedList',
                'blockQuote',
                'imageUpload',
            ],
        },
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
