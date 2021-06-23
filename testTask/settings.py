"""
Django settings for testTask project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
 
"""

import os 
import ldap
from django_auth_ldap.config import LDAPSearch, LDAPSearchUnion

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dx5au*5_72m&c-yrc*1)m)mh4g+^^36(-7%2ty@^1gr25da03s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'test_task'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'testTask.urls'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


PROJECT_TEMPLATES = [
    os.path.join(BASE_DIR, 'templates'),
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
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

WSGI_APPLICATION = 'testTask.wsgi.application'

AUTHENTICATION_BACKENDS = [
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
]

LDAP_SERVER = 'ldap.forumsys.com:389'
AUTH_LDAP_SERVER_URI = 'ldap://' + LDAP_SERVER
AUTH_LDAP_BIND_DN = 'cn=read-only-admin,dc=example,dc=com'
AUTH_LDAP_BIND_PASSWORD = "password"
 

#  TESTING
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# /!\ Note the filterstr on sAMAccountName this won't work otherwise /!\
AUTH_LDAP_USER_SEARCH = LDAPSearchUnion(
    LDAPSearch("OU=UTILISATEURS EGIS,DC=egis,dc=racine,dc=local",
               ldap.SCOPE_SUBTREE,
               filterstr='(sAMAccountName=%(user)s)'
               ),
    LDAPSearch("OU=UTILISATEURS EXTERNES,DC=egis,dc=racine,dc=local",
               ldap.SCOPE_SUBTREE,
               filterstr='(sAMAccountName=%(user)s)'
               ),
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
}


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'en' #default language 

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# //---Abhimanoj.Yadav

# Code added line 1..
# Code added line 2..
# Code added line 2..
# Code added line 3..
# Code added line 4..
# Code added line 5..
# 
