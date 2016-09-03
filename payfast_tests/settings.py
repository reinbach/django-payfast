import django
import os
import sys

from distutils.version import StrictVersion

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


def join(path):
    return os.path.abspath(os.path.join(PROJECT_ROOT, path))


# use package from the folder above, not the installed version
sys.path.insert(0, join('..'))

# ===== payfast settings ====

PAYFAST_MERCHANT_ID = '10000100'
PAYFAST_MERCHANT_KEY = '46f0cd694581a'

# ===========================

DEBUG = True

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join('db.sqlite'),
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = join('media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
SECRET_KEY = '5mcs97ar-(nnxjok67290+0^sr!e(ax=x$2-!8dqy25ff-l1*a='

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

if django.get_version() >= StrictVersion("1.8"):
    TEMPLATES = [
        {
            "BACKEND": 'django.template.backends.django.DjangoTemplates',
            'DIRS': (join('templates'),),
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                ],
            }
        }
    ]
else:
    TEMPLATE_DEBUG = DEBUG
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
    TEMPLATE_DIRS = (join('templates'),)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'payfast',
]

if django.VERSION < (1, 7):
    # test migrations if South is available
    try:
        import south  # noqa
        if 'south' not in INSTALLED_APPS:
            INSTALLED_APPS += ['south']
    except ImportError:
        pass
    else:
        del south
del django
