from .common import *  # noqa F403

# Application definition

SECRET_KEY = "5z!=r3pah3sdi1%3)@317*vnwdswra8lxyrz8175&q8z%6%z&a"

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.UnsaltedMD5PasswordHasher",
]


# Storages

STATICFILES_STORAGE = "server.storages.StaticStorage"
DEFAULT_FILE_STORAGE = "server.storages.MediaStorage"

AWS_DEFAULT_ACL = None
