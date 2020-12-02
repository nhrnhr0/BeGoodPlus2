"""
Django settings for begoodPlus project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from . import secrects

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '#r*r40h()nfz(8duh2%98n2=2y$!7hd6law4t#_mkht3xafe(c'
SECRET_KEY = secrects.SECRET_KEY
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

MY_DOMAIN = 'https://ms-global.co.il' #'http://127.0.0.1:8000'


# Application definition

INSTALLED_APPS = [


    # 3rd party
    'colorfield',
    'rest_framework',
    'django_user_agents',
    'django_extensions',
    'django_admin_index',
    'ordered_model',
    'admin_adv_search_builder',
    'mptt',
    'django_mptt_admin',
    'adminsortable',
    'admin_numeric_filter',
    #'jet',

    # own
    'core',
    'color',
    'provider',
    'category',
    'productColor',
    'productSize',
    'productImages',
    'product',
    'packingType',
    'stock',
    'order',
    'order_detail',
    'glofa_types',
    'order_detail_addons',
    'catalogImages',
    'catalogAlbum',
    'clientLikedImages',


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #'debug_toolbar', # TODO: remove in production
]
# django_user_agents implementation
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


MIDDLEWARE = [
    #'debug_toolbar.middleware.DebugToolbarMiddleware', # TODO: remove in production
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # own
    #'django.middleware.locale.LocaleMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    
]

# TODO: remove in production (SQL debug)
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]


ROOT_URLCONF = 'begoodPlus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static_cdn','templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                #'django.core.context_processors.request', #my code
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # own
                'pages.context_processors.navbar_load',
            ],
        },
    },
]

WSGI_APPLICATION = 'begoodPlus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'he'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/



LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]


STATIC_ROOT= os.path.join(BASE_DIR, "static") # when changed, change allso templates location
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_cdn"),
]

MEDIA_URL= '/media/'
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media_root/')
'''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = "ronionsegal@gmail.com"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_POST = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = "6464Ff8@@"
'''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'email-smtp.us-east-2.amazonaws.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = secrects.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD =  secrects.EMAIL_HOST_PASSWORD

# from django.core.mail import send_mail
# send_mail(subject='hey', message='message', from_email='bot@ms-global.co.il', recipient_list=['nhrnhr0@gmail.com'])