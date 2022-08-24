from xml.etree.ElementInclude import include
from django.urls import path
from django.urls.conf import include
from first_app import views

urlpatterns = [
    path('first_proj/', include('first_app.urls')),
]
