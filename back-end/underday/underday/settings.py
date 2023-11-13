
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#로컬
# SECRET_KEY = 'django-insecure-c8+a)c_rp1uk=cx*=rybzh(7ag%a2&_f54dp+xz#5vhght1ny8'
# 개발
SECRET_KEY = '5xeuu%71e@wu=#f@^xs6fp0d$adc@c7dvk@8-gfb%0r@ynpe*-'
# 운영
# SECRET_KEY = os.environ["DJANGO_SECRET"],

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
    'drf_yasg',
    'rest_framework',
    'main',
    'corsheaders',
    'user',
    'ticket',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:3000'
#                          ,'http://localhost:3000'
#                          ]
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'underday.urls'

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

WSGI_APPLICATION = 'underday.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
#로컬DB
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'underday',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
#개발DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'underday',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'svc.sel5.cloudtype.app',
        'PORT': '30518',
    }
# DATABASES = {
#      'default': {
#         'ENGINE': os.environ["DB_ENGINE"],
#         'NAME': os.environ["DATABASE"],
#         'USER': os.environ["DB_USER"],
#         'PASSWORD': os.environ["DB_PASSWORD"],
#         'HOST': os.environ["DB_HOST"],
#         'PORT': os.environ["DB_PORT"],
#     }  


 }



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

