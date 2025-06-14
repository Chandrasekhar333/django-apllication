"""
Django settings for Simple-Extraction-Demo-Track project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# IMPORTANT: Keep the secret key used in production secret!
# Get SECRET_KEY from environment variables for security.
SECRET_KEY = os.environ.get('tf=@th6bie_9yifz63l^3ousq3v(sp05a=1nw&(px*1yogj@z!', 'django-insecure-your-fallback-secret-key-for-local-testing-only')
# You should generate a strong random key and set it in your app.yaml (and never commit it).
# Example generation: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'


# SECURITY WARNING: don't run with debug turned on in production!
# Set DEBUG to False in production via environment variable.
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS for your App Engine application.
# It's good practice to explicitly list your App Engine URL.
# 'localhost' and '127.0.0.1' are included for running management commands locally if needed.
ALLOWED_HOSTS = [
    os.environ.get('GAE_APPLICATION_URL_HOST', '127.0.0.1'), # Default to localhost if env var not set (e.g., local management commands)
    'localhost',
    '127.0.0.1'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Your project's apps would go here
    # e.g., 'your_app_name',
    'rest_framework', # If you are using Django REST Framework
    'django_filters', # If your models/APIs use filtering
    # Add any other apps your project requires here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Only if you decided to use Whitenoise locally, not for GCS
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Simple-Extraction-Demo-Track.urls'

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

WSGI_APPLICATION = 'Simple-Extraction-Demo-Track.wsgi.application'


# Database Configuration (ONLY for Google App Engine)
# This configuration relies on environment variables set in app.yaml
# and uses the Cloud SQL Proxy automatically managed by App Engine.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Uses mysqlclient
        'NAME': os.environ.get('djang_db'),     # Name of the database (e.g., 'extraction_db')
        'USER': os.environ.get('djang_user'),     # Username for the database (e.g., 'django_user')
        'PASSWORD': os.environ.get('Chandu1'), # Password for the database user
        # 'HOST' points to the Unix socket for the Cloud SQL Proxy
        'HOST': '/cloudsql/{}'.format(os.environ.get('new-test-project-26417:us-central1:mydb')),
        'PORT': '', # PORT is not needed when connecting via Unix socket
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", # Recommended for MySQL
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# Google Cloud Storage Configuration for Static and Media Files
# Ensure 'django-storages' and 'google-cloud-storage' are in requirements.txt
GS_BUCKET_NAME = os.environ.get('my_bucket3849') # The name of your GCS bucket (e.g., 'your-app-bucket')
GS_DEFAULT_ACL = 'publicRead' # Make files publicly readable (important for static assets)

# STATIC_URL will point to your GCS bucket for static files
STATIC_URL = f'https://storage.googleapis.com/my_bucket3849/static/'
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

# MEDIA_URL will point to your GCS bucket for media files (user-uploaded)
MEDIA_URL = f'https://storage.googleapis.com/my_bucket3849/media/'
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# settings.py
# ...
ALLOWED_HOSTS = [
    os.environ.get('new-test-project-26417.uc.r.appspot.com', '127.0.0.1'),
    'localhost',
    '127.0.0.1'
]
# ...