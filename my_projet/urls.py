

from django.contrib import admin
from django.urls import path, include
from re import I
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('my_app.urls')),
]
