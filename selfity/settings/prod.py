from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        "CLIENT": {
           "name": 'selfity',
           "host": 'mongodb+srv://jchavez:kub0s911@cluster0.sqozq.mongodb.net/selfity?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority',
           "username": 'jchavez',
           "password": 'kub0s911',
           "authMechanism": "SCRAM-SHA-1",
        }, 
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR.child('static')
STATICFILES_DIRS = [BASE_DIR.child('staticfiles')]

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755
FILE_UPLOAD_PERMISSIONS = 0o644
