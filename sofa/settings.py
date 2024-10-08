"""
Django settings for sofa project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9vrbtl2)3up#=37ec5g9npur23hd@1wz^p+u@kmscd6-s0*e=2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'data',
    'django_extensions'
    # 'django_celery_beat',
    # 'django_celery_results',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sofa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'sofa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#         'OPTIONS': {
#             'timeout': 60,  # 30 saniyeye çıkarabilirsiniz
#         }
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Veritabanı motoru olarak SQLite kullanılır
        'NAME': BASE_DIR / 'db.sqlite3',         # Veritabanı dosyasının adı ve konumu
    }
}




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'django_proje',
#         'USER': 'mydjango',
#         'PASSWORD': 'dicle123',
#         'HOST': 'localhost',
#         'PORT': '5432',
        
#          'TEST': {
#             'NAME': 'existing_test_db',  # Mevcut bir veritabanı ismi girin
#             'MIRROR': 'default',  # Testler, mevcut veritabanını kullanacak
#          }
         
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/


# Django settings.py
TIME_ZONE = 'Europe/Istanbul'


LANGUAGE_CODE = 'tr-tr'



USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CELERY_BROKER_URL = 'redis://localhost:6379/0'  # RabbitMQ yerine Redis kullanıyoruz
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # Sonuçları da Redis'te saklayacağız
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Europe/Istanbul'
# CELERY_ENABLE_UTC = True
# CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True







# # Celery Ayarları
#CELERY_BROKER_URL = 'amqp://localhost'  # RabbitMQ kullanıyorsanız bu şekilde
# CELERY_BEAT_SCHEDULE = {
#     'add-tournaments-every-minute': {
#         'task': 'myapp.tasks.add_tournaments_from_excel',
#         'schedule': 60.0,  # 60 saniye, yani dakikada bir
#         'args': ('"/home/ahmet/Masaüstü/DjangoPro/testdata/Tournament.xlsx',)  # Excel dosyanızın yolunu buraya yazın
#     },
# }


# from celery.schedules import crontab

# CELERY_BEAT_SCHEDULE = {
#     'deneme-task-every-minute': {
#         'task': 'myapp.tasks.add_tournaments_from_excel',
#         'schedule': crontab(minute='*', hour='*', day_of_month='*', month_of_year='*', day_of_week='0-6'),  # Dakikada bir çalışır, her gün
#         'timezone': 'Europe/Istanbul'  # İstanbul zaman diliminde çalışacak
#     },
# }

# CELERY_TIMEZONE = 'Europe/Istanbul'

# DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000
# settings.py
# CELERY_TASK_ALWAYS_EAGER = True # Doğru port numarasını kontrol edin
# CELERY_TASK_EAGER_PROPAGATES = True
