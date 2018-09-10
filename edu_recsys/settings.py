"""
Django settings for edu_recsys project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import json
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'edu_recsys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'edu_recsys.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'PAGE_SIZE': 5
}
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"

STATIC_ROOT = '/var/www/edu_recsys/static/'
STATIC_URL = '/static/'
INSTALLED_APPS += ("rest_framework", "coreapi")
INSTALLED_APPS += ("apps.context", "apps.core", "apps.activity", "apps.digital_profile", 'apps.interpreter', 'apps.networking')

CONFIG = json.loads(open(os.path.join(BASE_DIR, 'config.json')).read())

DEBUG = CONFIG.get("DEBUG", False)

norm_url = lambda x: x[:-1] if x[-1]=='/' else x

LABS_BASE_URL = norm_url(CONFIG["LABS_BASE_URL"])
LABS_APP_TOKEN = CONFIG["LABS_APP_TOKEN"]

DP_BASE_URL = norm_url(CONFIG["DP_BASE_URL"])
DP_APP_TOKEN = CONFIG["DP_APP_TOKEN"]


PLE_BASE_URL = norm_url(CONFIG["PLE_BASE_URL"])
PLE_APP_TOKEN = CONFIG["PLE_APP_TOKEN"]
PLE_GUID_UUIDS = CONFIG["PLE_GUID_UUIDS"]

LRS_BASE_URL = norm_url(CONFIG["LRS_BASE_URL"])
LRS_AUTH_TOKEN = CONFIG["LRS_AUTH_TOKEN"]
LRS_ARCHETYPES_GUID = CONFIG["LRS_ARCHETYPES_GUID"]

DIAGNOSTICS_V0_GUID_TO_COMMON = CONFIG["DIAGNOSTICS_V0_GUID_TO_COMMON"]
DIAGNOSTICS_V0_NORM = CONFIG["DIAGNOSTICS_V0_NORM"]
_default_mu = dict((k,0) for k in DIAGNOSTICS_V0_NORM.keys())
DIAGNOSTICS_V0_MU = CONFIG.get("DIAGNOSTICS_V0_MU", _default_mu)

DIRECTION_UUIDS = CONFIG["DIRECTION_UUIDS"]
NETWORKING_MIN_NUMBER_START = CONFIG.get('NETWORKING_MIN_NUMBER_START', 3)

API_KEY = CONFIG["API_KEY"]

ALLOWED_HOSTS = CONFIG["ALLOWED_HOSTS"]

SECRET_KEY = CONFIG.get("SECRET_KEY", 'SECRET_KEY')

DATABASES = {
    'default': CONFIG["DATABASE"],
}

BROKER_URL = CONFIG["BROKER_URL"]

CELERY_TASK_SERIALIZER = "pickle"
CELERY_ACCEPT_CONTENT = ['pickle']

if DEBUG:
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    INTERNAL_IPS = ('127.0.0.1',)

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
    )

    INSTALLED_APPS += ("debug_toolbar",)

    # hack - sql3 for local tests
    if 'test' in sys.argv:
        DATABASES['default'] = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
