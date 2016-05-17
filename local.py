import os
from .common import *

MEDIA_URL = "http://{{public_hostname}}/media/"
STATIC_URL = "http://{{public_hostname}}/static/"
ADMIN_MEDIA_PREFIX = "http://{{public_hostname}}/static/admin/"
SITES["front"]["scheme"] = "http"
SITES["front"]["domain"] = "{{public_hostname}}"

SECRET_KEY = '{{secret_key}}'

DEBUG = False
TEMPLATE_DEBUG = False
PUBLIC_REGISTER_ENABLED = {{public_register_enabled}}

DEFAULT_FROM_EMAIL = '{{default_from}}'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': '{{database_name}}',
		'USER': '{{database_user}}',
		'PASSWORD': '{{database_password}}',
		'HOST': '{{database_host}}',
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
			'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
		},
	},
}

# Uncomment and populate with proper connection parameters
# for enable github login/singin.
# GITHUB_API_CLIENT_ID = "yourgithubclientid"
# GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"
