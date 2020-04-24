from django.contrib import admin

from actividad.models import Actividad


class AdminActividad(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_hora']


admin.site.register(Actividad, AdminActividad)
