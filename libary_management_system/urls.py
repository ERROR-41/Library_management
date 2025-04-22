from django.contrib import admin
from django.urls import path, include
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api/v1/", include("library.urls"), name="api-root"),
    path('',views.api_root_view)
] + debug_toolbar_urls()
