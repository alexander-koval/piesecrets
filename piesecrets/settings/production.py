import environ
from .base import *

root = environ.Path(__file__) - 3  # get root of the project
env = environ.Env()
# environ.Env.read_env()  # reading .env file
SITE_ROOT = root()
DEBUG = env.bool('DEBUG', default=False)
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = env.str('SECRET_KEY')

DJANGO_ALLOWED_HOSTS = str(env.str('DJANGO_ALLOWED_HOSTS', ""))
ALLOWED_HOSTS = DJANGO_ALLOWED_HOSTS.split(" ") 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
