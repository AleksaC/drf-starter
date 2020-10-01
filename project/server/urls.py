"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("health-check/", include("health_check.urls")),
    path("admin/", admin.site.urls),
    path("users/", include(("users.urls", "users"))),
    path(
        "auth/",
        include(
            [
                path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
                path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
                path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
            ],
        ),
    ),
]

if settings.DEBUG:
    import debug_toolbar
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view

    schema_view = get_schema_view(
        openapi.Info(
            title="drf-base",
            default_version="v1",
            description="drf boilerplate",
            contact=openapi.Contact(email="aleksacukovic1@gmail.com"),
        ),
        public=False,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns = [
        *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
        path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
