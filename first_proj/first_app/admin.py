from django.contrib import admin
from .models import  Pagina, Topico, Webpage

admin.site.register(Topico)
admin.site.register(Webpage)
admin.site.register(Pagina)