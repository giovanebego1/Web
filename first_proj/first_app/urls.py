from unicodedata import name
from django.urls import path
from django.urls.conf import include
from . import views, urls

urlpatterns = [
    path('index/', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('base/', views.base, name="base"),
    path('calculadora/', views.calculadora, name="calculadora"),
    path('form/', views.first_form, name='first_form'),
    path('web/', views.web, name='web'),
]