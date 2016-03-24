from .common import *
import os

MEDIA_URL = "http://taiga.benjamin-borbe.de/media/"
STATIC_URL = "http://taiga.benjamin-borbe.de/static/"
ADMIN_MEDIA_PREFIX = "http://taiga.benjamin-borbe.de/static/admin/"
SITES["front"]["scheme"] = "http"
SITES["front"]["domain"] = "taiga.benjamin-borbe.de"

SECRET_KEY = '{{secret_key}}'

DEBUG = False
TEMPLATE_DEBUG = False
PUBLIC_REGISTER_ENABLED = False

DEFAULT_FROM_EMAIL = "smtp@benjamin-borbe.de"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

DATABASES = {
	'default': {
		'ENGINE': 'transaction_hooks.backends.postgresql_psycopg2',
		'NAME': '{{database_name}}',
		'USER': '{{database_user}}',
		'PASSWORD': '{{database_password}}',
		'HOST': '{{database_hostname}}',
		'PORT': '{{database_port}}',
	}
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_HOST = '{{smtp_host}}'
EMAIL_PORT = '{{smtp_port}}'
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'handlers': {
		'console': {
			'class': 'logging.StreamHandler',
		},
	},
	'loggers': {
		'django': {
			'handlers': ['console'],
			'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
		},
	},
}

# Uncomment and populate with proper connection parameters
# for enable github login/singin.
# GITHUB_API_CLIENT_ID = "yourgithubclientid"
# GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"
