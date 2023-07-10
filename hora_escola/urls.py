from django.contrib import admin
from django.urls import path
from django.urls import include, path
from hora_escola.core import urls as core_urls

urlpatterns = [
    path('', include(core_urls)),
    path('admin/', admin.site.urls),
]