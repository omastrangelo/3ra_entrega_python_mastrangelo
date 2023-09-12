from django.contrib import admin
from .models import Trabajo, Trabajador, Entregas
# Register your models here.

admin.site.register(Trabajo)
admin.site.register(Trabajador)
admin.site.register(Entregas)