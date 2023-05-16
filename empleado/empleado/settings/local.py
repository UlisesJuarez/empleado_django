from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'dbempleado',
        'USER':'uligod',
        'PASSWORD':'uligod123',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

STATIC_URL = 'static/'
STATICFILES_DIRS = [
        os.path.join (BASE_DIR, "static"),
]

#para que se guarden las imagenes o media de los modelos
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join (BASE_DIR, "media")