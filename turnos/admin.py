from django.contrib import admin
from .models import Medico , Turno

class TurnoAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido', 'dni' , 'medico' )

admin.site.register(Medico)
admin.site.register(Turno, TurnoAdmin)