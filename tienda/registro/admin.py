from django.contrib import admin
from .models import Reporte


class ReporteAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    
# Register your models here.

admin.site.register(Reporte, ReporteAdmin)
