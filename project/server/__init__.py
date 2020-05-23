import os

# This will ensure that the app settings are set to production when gunicorn is
# used as this is the first module that gets executed making the settings set in
# celery app the ones used for the whole app
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings.prod")  # noqa: E402

# This will ensure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ("celery_app",)
