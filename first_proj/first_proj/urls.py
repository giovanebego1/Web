import imp
from xml.etree.ElementInclude import include
from django.urls import path
from django.urls.conf import include
from first_app import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_proj/', include('first_app.urls')),
]
