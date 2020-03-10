from . import *
import logging 
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration 

DEBUG = False
ALLOWED_HOSTS = ['204.48.26.176']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'projet8',
        'USER': 'nathansql',
        'PASSWORD': os.environ.get('SQLPWD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

sentry_logging = LoggingIntegration( 
    level=logging.INFO, # Capture info and above as breadcrumbs 
    event_level=logging.ERROR # Send errors as events 
) 

sentry_sdk.init(
    dsn="https://0b44cc663eaa4f35b107cbdd75719913@sentry.io/2827010",
    integrations=[DjangoIntegration(), sentry_logging],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=False,
    environment="production"
)
