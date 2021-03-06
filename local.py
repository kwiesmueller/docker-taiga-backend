import os
from .common import *

MEDIA_URL = "https://{{public_hostname}}/media/"
STATIC_URL = "https://{{public_hostname}}/static/"
ADMIN_MEDIA_PREFIX = "https://{{public_hostname}}/static/admin/"
SITES["front"]["scheme"] = "https"
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
EMAIL_USE_TLS = {{smtp_tls}}
EMAIL_USE_SSL = {{smtp_ssl}}
EMAIL_HOST = '{{smtp_host}}'
EMAIL_PORT = '{{smtp_port}}'
EMAIL_HOST_USER = "{{smtp_user}}"
EMAIL_HOST_PASSWORD = "{{smtp_password}}"

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
