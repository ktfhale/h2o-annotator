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

    # apps
    'main',
    'search',

    # third party
    'django_extensions',
    'crispy_forms',
    'rest_framework',
    'webpack_loader',
    'django_json_widget',

    # built-in
    'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'main.middleware.method_override_middleware',

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'main.middleware.AuthenticationMiddleware',
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
                'config.context_processors.settings',
                'config.context_processors.frontend_urls',
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


AUTH_USER_MODEL = 'main.User'


# Password validation - https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
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

# LIL's analytics JS
USE_ANALYTICS = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
GUIDE_URL = 'https://about.opencasebook.org/'
BLOG_URL = 'https://about.opencasebook.org/blog/'
VIDEO_URL = 'https://about.opencasebook.org/other-resources'
TWITTER_URL= 'https://twitter.com/opencasebook'
CAPAPI_CASE_URL_FSTRING = 'https://api.case.law/v1/cases/{}/'
CAPAPI_COURT_URL_FSTRING = 'https://api.case.law/v1/courts/?id={}'

CONTACT_EMAIL = 'info@opencasebook.org'
DEFAULT_FROM_EMAIL = 'info@opencasebook.org'
PROFESSOR_VERIFIER_EMAILS = ['info@opencasebook.org']

# Make these settings available for use in Django's templates.
# e.g. <a href="mailto:{{ CONTACT_EMAIL }}">Contact Us</a>
TEMPLATE_VISIBLE_SETTINGS = (
    'USE_ANALYTICS',
    'CONTACT_EMAIL',
    'GUIDE_URL',
    'BLOG_URL',
    'VIDEO_URL',
    'TWITTER_URL'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level':'INFO',
            'filters': ['require_debug_false'],
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '/tmp/h2o.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'main.reporter.CustomAdminEmailHandler'
        },
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
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(filename)s %(lineno)d: %(message)s'
        },
    },
    'filters': {
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse'
         }
     },
}

# avoid the need for collectstatic in production (see http://whitenoise.evans.io/en/stable/django.html#WHITENOISE_USE_FINDERS )
WHITENOISE_USE_FINDERS = True

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}

CAPAPI_BASE_URL = 'https://api.case.law/v1/'
CAPAPI_API_KEY = ''


CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = False

# Temporary: this is the name of the CSRF header used by the Rails app's AJAX requests
CSRF_HEADER_NAME = 'HTTP_X_CSRF_TOKEN'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',  # authenticate with Django login
    ),
}

PANDOC_DIR = os.path.join(os.path.dirname(BASE_DIR), 'services/pandoc')

PASSWORD_HASHERS = [
    # this is the standard recommended Django password hasher; first item on this list will be used for all new logins
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    # legacy password hasher for users who haven't logged in since Rails migration
    'main.hashers.PBKDF2WrappedRailsPasswordHasher',
]
