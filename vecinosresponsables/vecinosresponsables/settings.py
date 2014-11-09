"""
Django settings for vecinosresponsables project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2rm&qw8f^04!$8)5r5tg$-6ycjpis1u+*is!h@&ytc-k3=y$67'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vecinosapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'vecinosresponsables.urls'

WSGI_APPLICATION = 'vecinosresponsables.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR, 'vecinosapp/static/')

STATIC_ROOT = ''

STATIC_URL = '/static/'

# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
'django.contrib.staticfiles.finders.FileSystemFinder',
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = os.path.join(BASE_DIR, 'static/uploads'),
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/uploads/'

ADMIN_MEDIA_PREFIX = '/static/admin'

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/vecinosresponsables'