from django.contrib import admin
from tipo.models import Tipo

# Register your models here.

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ['nombre']