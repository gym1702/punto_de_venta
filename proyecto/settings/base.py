from pathlib import Path
import secrets
#import pytz

from django.core.exceptions import ImproperlyConfigured
import json

from django.contrib.messages import constants as messages




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


#******************************************************
#    CONFIGURACION PARA LEER EL SECRET.JSON
#******************************************************
with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = 'La variable %s no existe' % secret_name
        raise ImproperlyConfigured(msg)
#*******************************************************


SECRET_KEY = get_secret('SECRET_KEY')


#CONFIGURACION NECESARIA PARA MENSAJERIA
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #"django_cron",
    'django.contrib.humanize',
    

]

LOCAL_APPS = [
    'applications.home',
    'applications.users',
    'applications.empresa',  
    'applications.clientes', 
    'applications.categorias',
    'applications.marcas',
    'applications.proveedores',
    'applications.productos', 
    'applications.ventas',

    # 'applications.medicos',    
    # 'applications.expedientes',    
    # 'applications.citas',
    # 'applications.asistentes',
    # 'applications.secretarias',
    # 'applications.servicios',
    # 'applications.medicamentos',
    # 'applications.presupuestos',
    # 'applications.recetas',    
    # 'applications.consentimiento',
    # 'applications.mantto',
]

THIRD_PARTY_APPS = [
    #'fontawesomefree',
    #'django_extensions',
    #'import_export',
    'sweetify',
    #'scheduler',
    #'smart_selects',
    #'rest_framework',
]


INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

#SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'

#AGREGAR ESTA VARIABLE PARA ARCHIVOS ESTATICOS EN PRODUCCION
# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# ]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #PAQUETE PARA CERRAR SESION POR INACTIVIDAD (INSTALAR django-session-timeout)
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]


ROOT_URLCONF = 'proyecto.urls'

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


WSGI_APPLICATION = 'proyecto.wsgi.application'


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


#****************************************************************************
# INDICAMOS QUE ESTA CONFIGURACION SE HARA CARGO DE LOS USUARIOS DEL SISTEMA
#****************************************************************************
AUTH_USER_MODEL = 'users.User'




# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#CIERRE DE SESION EN SEGUNDOS (inatalar django-session-timeout)
SESSION_EXPIRE_SECONDS = 28800 # (8 HRS) (3600seg x 8hrs = 14400)
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_TIMEOUT_REDIRECT = 'users_app:login'



#PARA PROGRAMACION DE TAREAS
#UTILIZANDO CRON
# CRON_CLASSES = [
#     'applications.pacientes.cron.EnviarFelicitacionCumpleanos',
#     'applications.citas.cron.EnviarRecordatorioCita',
# ]


#TOKEN TWILIO PARA WHATSAPP
# TWILIO_ACCOUNT_SID = 'AC186a15c229671527c70e1f0b513a52cd'
# TWILIO_AUTH_TOKEN = '8f3f7032f67219ffc9872ef83afd98f6'
# TWILIO_PHONE_NUMBER = 'whatsapp:+18146373335'


#TOKEN TWILIO NUEVA CUENTA (dentalzac01@gmail.com) PARA WHATSAPP
# TWILIO_ACCOUNT_SID = 'AC92b41c3076fcd97636736886efdf0986'
# TWILIO_AUTH_TOKEN = '649ea30d725f40aa29bc3196ff533d1c'
# TWILIO_PHONE_NUMBER = 'whatsapp:+18642147755'