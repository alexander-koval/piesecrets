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

PATH_TO_LOG = '/var/log/piesecrets'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'fmt': {
            'format':'%(asctime)s %(levelname)-5s (%(name)s) %(message)s',
            'datefmt':'%Y-%m-%d %H:%M:%S'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        '__main__': {
            'handlers': ['informator', 'warnator', 'errormator'],
            'level': 'INFO',
            'propagate': True,
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'informator': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename':'%s/info.log'%PATH_TO_LOG,
            'formatter':'fmt'
        },
        'warnator': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename':'%s/warning.log'%PATH_TO_LOG,
            'formatter':'fmt'
        },
        'errormator': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename':'%s/error.log'%PATH_TO_LOG,
            'formatter':'fmt'
        },
    }
}

try:
    from .local import *
except ImportError:
    pass
