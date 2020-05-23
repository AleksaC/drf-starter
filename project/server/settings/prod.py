import os

from .common import *  # noqa F403

# Application definition

DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    # Starts with dot to include subdomains
    f".{os.environ['DOMAIN_NAME']}",
]

SECRET_KEY = os.environ["SECRET_KEY"]


# Databases

# This may cause problems depending on your database/connection pooler configuration
# read more here: https://docs.djangoproject.com/en/3.0/ref/databases/#persistent-connections
# Using persistent connections may cause problems with celery so you should
# export DB_CONN_MAX_AGE=0 before running the worker
# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html#known-issues
CONN_MAX_AGE = os.environ.get("DB_CONN_MAX_AGE")
DATABASES["default"]["CONN_MAX_AGE"] = (
    CONN_MAX_AGE if CONN_MAX_AGE is None else int(CONN_MAX_AGE)
)
# Remove if not using PgBouncer with transaction pool_mode
DISABLE_SERVER_SIDE_CURSORS = True


# Storages

STATICFILES_STORAGE = "server.storages.StaticStorage"
DEFAULT_FILE_STORAGE = "server.storages.MediaStorage"


# E-mail

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
SERVER_EMAIL = f"Error error@{os.environ['DOMAIN_NAME']}"


# Administration

ADMINS = [("Aleksa", "aleksacukovic1@gmail.com")]


# Security

SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_REFERRER_POLICY = "same-origin"


# DRF

REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer",],
}


# Simple JWT

SIMPLE_JWT = {
    "SIGNING_KEY": os.environ["JWT_SIGNING_KEY"],
}


# django-storages

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]

AWS_S3_REGION_NAME = os.environ["AWS_S3_REGION_NAME"]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
AWS_S3_CUSTOM_DOMAIN = os.environ["CLOUDFRONT_DOMAIN_NAME"]

AWS_DEFAULT_ACL = None


# Anymail

ANYMAIL = {
    "MAILGUN_API_KEY": os.environ["MAILGUN_API_KEY"],
    "MAILGUN_SENDER_DOMAIN": f"mg.{os.environ['DOMAIN_NAME']}",
}
