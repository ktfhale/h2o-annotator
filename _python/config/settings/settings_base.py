"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',

    # built-in
    'main.apps.CustomAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'main',
    'search',

    # third party
    'django_extensions',
    'crispy_forms',
]

MIDDLEWARE = [
    'main.middleware.generated_by_header_middleware',
    'main.middleware.method_override_middleware',

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',  # sets request.session
    'main.middleware.rails_session_middleware',  # sets request.rails_session

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    # this gets overridden by rails_auth_middleware, but django admin will complain if it's taken out
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'main.middleware.rails_auth_middleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
                'config.context_processors.settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Temmporary:
# From the warning messages we are getting, I think the timestamps
# in the DB from the Rails application do not have timezone info.
# Let's plan to migrate, once we are fully python.
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

RAILS_SECRET_KEY_BASE = None

LOGIN_URL = '/user_sessions/new'
SIGNUP_URL = '/users/new'
GUIDE_URL = 'https://about.opencasebook.org/'
BLOG_URL = 'https://about.opencasebook.org/blog/'
CAPAPI_CASE_URL_FSTRING = 'https://api.case.law/v1/cases/{}/'
CAPAPI_COURT_URL_FSTRING = 'https://api.case.law/v1/courts/?id={}'

CONTACT_EMAIL = 'info@opencasebook.org'


# Make these settings available for use in Django's templates.
# e.g. <a href="mailto:{{ CONTACT_EMAIL }}">Contact Us</a>
TEMPLATE_VISIBLE_SETTINGS = (
    'LOGIN_URL',
    'SIGNUP_URL',
    'CONTACT_EMAIL',
    'GUIDE_URL',
    'BLOG_URL'
)


AUTH_USER_MODEL = 'main.User'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s module=%(module)s, '
                      'process_id=%(process)d, %(message)s'
        }
    },
}


# serve Rails public/ folder at the root, so urls like /robots.txt and /packs/css/main.css will work:
WHITENOISE_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'public')

# avoid the need for collectstatic in production (see http://whitenoise.evans.io/en/stable/django.html#WHITENOISE_USE_FINDERS )
WHITENOISE_USE_FINDERS = True

CAPAPI_BASE_URL = 'https://api.case.law/v1/'
CAPAPI_API_KEY = ''


# Set this to true to affirmatively assert that it is OK to execute code that includes fix_before_deploy() lines.
# This can safely be set to True everywhere except on production.
NOT_ON_PRODUCTION = False

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = False

# Temporary: this is the name of the CSRF header used by the Rails app's AJAX requests
CSRF_HEADER_NAME = 'HTTP_X_CSRF_TOKEN'
