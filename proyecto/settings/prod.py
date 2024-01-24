from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!

#comentar para despliegue, en local activar
DEBUG = False

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://*.glsoft.com.mx', 'https://*.127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS = [BASE_DIR / "static",]

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]

#STATIC_ROOT = (BASE_DIR / "staticfiles")
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = (BASE_DIR / 'media')



#EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_secret('EMAIL')
EMAIL_HOST_PASSWORD = get_secret('EMAIL_PASSWORD')
EMAIL_PORT = 587


#PARA PERMITIR HTTPS
# SECURE_SSL_REDIRECT=False
# SESSION_COOKIE_SECURE=False
# CSRF_COOKIE_SECURE=False




