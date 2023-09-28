"""
Django settings for permatopia_site project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import secrets

import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# added secret key to heroku config - generated by Djecrety
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get(
#     "DJANGO_SECRET_KEY",
#     default=secrets.token_urlsafe(nbytes=64),
# )
# SECRET_KEY = 'django-insecure-_hib^w!pns-=ea+l3k0e=nv##_9mj)_ij0&bgs5x13k(r4=s7+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG_PROPAGATE_EXCEPTIONS = True


ALLOWED_HOSTS = ['https://simple-farm-tracking-5b0965f19d6e.herokuapp.com/','*']

IS_HEROKU_APP = "DYNO" in os.environ and not "CI" in os.environ


# Application definition

INSTALLED_APPS = [
    'farm_management_app.apps.FarmManagementAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_tables2',
    'django_filters',
    "django_htmx",
    'crispy_forms',
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware"
]

ROOT_URLCONF = 'permatopia_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',

                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.request",
                'farm_management_app.contextprocessor.curr_year',
            ],
        },
    },
]

WSGI_APPLICATION = 'permatopia_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if IS_HEROKU_APP:
    # In production on Heroku the database configuration is derived from the `DATABASE_URL`
    # environment variable by the dj-database-url package. `DATABASE_URL` will be set
    # automatically by Heroku when a database addon is attached to your Heroku app. See:
    # https://devcenter.heroku.com/articles/provisioning-heroku-postgres
    # https://github.com/jazzband/dj-database-url
    DATABASES = {
        "default": dj_database_url.config(
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True,
        ),
    }
else:
    # When running locally in development or in CI, a sqlite database file will be used instead
    # to simplify initial setup. Longer term it's recommended to use Postgres locally too.
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'ec2-52-215-68-14.eu-west-1.compute.amazonaws.com',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'de4jreh8k39fqt',
#         'USER': 'rectrzxzhdswtc',
#         'PASSWORD': '6aaa1204071a7b3d2566da0a953fa4aabcb8d6e7a40bf01495943376268bf0d5',
#         'HOST': 'ec2-52-215-68-14.eu-west-1.compute.amazonaws.com',
#         'PORT': '5432'
#     }
# }

# import dj_database_url
# db_from_env = dj_database_url.config(
#     conn_max_age=600,
#     conn_health_checks=True,
#     )
# DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = BASE_DIR / "staticfiles"


STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Crispy forms template
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"



BOOTSTRAP_DATEPICKER_PLUS = {
    "options": {
        "locale": "daDK",
    },
    "variant_options": {
        "date": {
            "format": "DD/MM/YYYY",
        },
    }
}


# whitenoise
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# users

AUTH_USER_MODEL = 'farm_management_app.User'
# AUTHENTICATION_BACKENDS = ['farm_management_app.User.UserBackend']
