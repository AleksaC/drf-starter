from storages.backends.s3boto3 import S3Boto3Storage

from django.conf import settings


class StaticStorage(S3Boto3Storage):
    location = settings.STATIC_ROOT
    file_overwrite = True


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIA_ROOT
    file_overwrite = False
