"""

Django settings for postscribers project.


Generated by 'django-admin startproject' using Django 4.1.7.


For more information on this file, see

https://docs.djangoproject.com/en/4.1/topics/settings/


For the full list of settings and their values, see

https://docs.djangoproject.com/en/4.1/ref/settings/
"""


from pathlib import Path
# import dj_database_url
import os 

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Build paths inside the project like this: BASE_DIR / 'subdir'.


load_dotenv(BASE_DIR / '.env')


# Quick-start development settings - unsuitable for production

# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = "django-insecure-#$d+m9y11yt_3w_2o^#x*94jjvih*1k4g@7d-e1x%j(8zv*89z"


# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = True


ALLOWED_HOSTS = ["*"]




# Application definition


INSTALLED_APPS = [

    "django.contrib.admin",

    "django.contrib.auth",

    "django.contrib.contenttypes",

    "django.contrib.sessions",

    "django.contrib.messages",

    "django.contrib.staticfiles",

    "blog",

    "crispy_forms",

    "crispy_bootstrap5",
    "users"

]


MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    

]

CSRF_TRUSTED_ORIGINS = ['https://naveenkumardongredjangoblog.up.railway.app',]



ROOT_URLCONF = "postscribers.urls"


TEMPLATES = [

    {

        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [BASE_DIR / "templates"],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.debug",

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],

        },

    },

]


WSGI_APPLICATION = "postscribers.wsgi.application"


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Database

# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {

    "default": {

        "ENGINE": "django.db.backends.sqlite3",

        "NAME": BASE_DIR / "db.sqlite3",

    }

}

# DATABASES = {
#     'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
# }



# Password validation

# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators


AUTH_PASSWORD_VALIDATORS = [

    {

        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",

    },

    {

        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",

    },

    {

        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",

    },

    {

        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",

    },

]



# Internationalization

# https://docs.djangoproject.com/en/4.1/topics/i18n/


LANGUAGE_CODE = "en-us"


TIME_ZONE = "UTC"


USE_I18N = True


USE_TZ = True


# Crispy form template pack added by Naveen

CRISPY_TEMPLATE_PACK = 'bootstrap5'

CRISPY_TEMPLATE_PACK = "bootstrap5"



# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/4.1/howto/static-files/


LOGIN_REDIRECT_URL = 'blog-index'


LOGIN_URL = 'users-login'



# Default primary key field type

# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"




STATIC_URL = '/static/'

MEDIA_ROOT = (BASE_DIR / 'media')

MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

STATIC_ROOT = (BASE_DIR / 'asset')




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.getenv('EMAIL_HOST')

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

EMAIL_PORT =  os.getenv('EMAIL_PORT')

EMAIL_USE_TLS = True





