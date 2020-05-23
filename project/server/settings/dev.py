from .common import *  # noqa F403

# Application definition

SECRET_KEY = "5z!=r3pah3sdi1%3)@317*vnwdswra8lxyrz8175&q8z%6%z&a"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += ["drf_yasg", "debug_toolbar"]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


# Debug toolbar

show_toolbar = lambda request: True  # noqa: E731

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": "server.settings.dev.show_toolbar",
}
