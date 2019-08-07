from .settings_base import *  # noqa

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '.local']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '***REMOVED***'

DEBUG = True

# don't check password quality locally, since it's annoying
AUTH_PASSWORD_VALIDATORS = []

if os.environ.get('DOCKERIZED'):
    DATABASES['default']['PASSWORD'] = 'password'
    DATABASES['default']['NAME'] = 'h2o_dev'


# avoid test errors when running tests locally, since pytest-django sets DEBUG=False and staticfiles/ doesn't exist
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
