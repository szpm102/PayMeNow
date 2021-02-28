"""
Django settings for paymesite project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_281q%ruv34r@veu_7npct#sg!0r=objk)1@&2g)_de!6+)d@b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'paymentlist',
    'bootstrap_datepicker_plus',
    'bootstrap4',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'django.contrib.sites',
    'microsoft_auth',
    'storages',
    'pwa_webpush',
    'django_user_agents',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]



ROOT_URLCONF = 'paymesite.urls'

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
                'microsoft_auth.context_processors.microsoft',
            ],
        },
    },
]

WSGI_APPLICATION = 'paymesite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': str(os.path.join(BASE_DIR, "db.sqlite3")),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': os.environ.get('DATABASE_PORT', ''),
    }
}
LOGIN_URL = "/login/"

ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_REQUIRED  = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
DEFAULT_HTTP_PROTOCOL = "https"
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Cache backend is optional, but recommended to speed up user agent parsing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'


#New Autehnication for Facebook

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': False,
        'LOCALE_FUNC': lambda request: 'en-US',
    }
}

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    'microsoft_auth.backends.MicrosoftAuthenticationBackend',
    "allauth.account.auth_backends.AuthenticationBackend",
)

MICROSOFT_AUTH_CLIENT_ID = '6d22bc9c-4803-4822-95f5-a6226881c3c1'
MICROSOFT_AUTH_CLIENT_SECRET = '~RcVQVU_F2~FPA-T-6bW4NXwePD_bpkGH8'
MICROSOFT_AUTH_LOGIN_TYPE = 'ma'
LOGIN_REDIRECT_URL = "/"

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/




#STATICFILES_DIRS = ( os.path.join('static'), )
#STATIC_ROOT = os.path.join(BASE_DIR,'static')

AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME', '')
AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY', '')
AZURE_CUSTOM_DOMAIN = os.environ.get('AZURE_CUSTOM_DOMAIN', '')
AZURE_LOCATION = os.environ.get('AZURE_LOCATION', '')
AZURE_CONTAINER = os.environ.get('AZURE_CONTAINER', '')
#STATIC_CONTAINER = os.environ.get('STATIC_CONTAINER', '')
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_LOCATION}/'
#STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_LOCATION}/'

DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
#STATICFILES_STORAGE = 'paymesite.custom_azure.PublicAzureStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = (os.path.join('static'), )

THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE

SITE_ID = 1


PWA_APP_NAME = 'Pay Me Now'
PWA_APP_DESCRIPTION = "App used to request payment for pruchases done on behalf of SZPM"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/paymesite/logo.jpg',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/paymesite/apple_icon.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/icons/splash-640x1136.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'


try:
    from .local_settings import *
    #INSTALLED_APPS += DEV_APPS
except ImportError:
    print ('Looks like no local file. You are on production')