from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('web/', views.web, name="web"),
    path('calculadora/', views.calculadora, name="calculadora"),

]