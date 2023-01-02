from django.contrib import admin
from .models import *

# Register your models here.

class CamposAdmin(admin.ModelAdmin):
    readonly_fields = ('created','modified')
    list_display = ('nombre', 'stock', 'modified')

admin.site.register(Productos_li, CamposAdmin)
admin.site.register(Insumos_li, CamposAdmin)