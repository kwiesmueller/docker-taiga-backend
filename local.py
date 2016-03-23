from .common import *

MEDIA_URL = "http://taiga.benjamin-borbe.de/media/"
STATIC_URL = "http://taiga.benjamin-borbe.de/static/"
ADMIN_MEDIA_PREFIX = "http://taiga.benjamin-borbe.de/static/admin/"
SITES["front"]["scheme"] = "http"
SITES["front"]["domain"] = "taiga.benjamin-borbe.de"

SECRET_KEY = "theveryultratopsecretkey"

DEBUG = False
TEMPLATE_DEBUG = False
PUBLIC_REGISTER_ENABLED = True

DEFAULT_FROM_EMAIL = "no-reply@benjamin-borbe.de"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

DATABASES = {
	'default': {
		'ENGINE': 'transaction_hooks.backends.postgresql_psycopg2',
		'NAME': 'taiga',
		'USER': 'taiga',
		'PASSWORD': 'Bri72GuWPpaly1qu',
		'HOST': 'taiga-postgres.default.svc.cluster.local',
		'PORT': '5432',
	}
}

# Uncomment and populate with proper connection parameters
# for enable email sending. EMAIL_HOST_USER should end by @domain.tld
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_USE_TLS = False
# EMAIL_HOST = "localhost"
# EMAIL_HOST_USER = ""
# EMAIL_HOST_PASSWORD = ""
# EMAIL_PORT = 25

# Uncomment and populate with proper connection parameters
# for enable github login/singin.
# GITHUB_API_CLIENT_ID = "yourgithubclientid"
# GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"
