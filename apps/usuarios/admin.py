from django.contrib import admin
from apps.usuarios.models import Salvas

class ListarSalvas(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fotografia')
    list_display_links = ('id',)
    search_fields = ('usuario', 'fotografia')
    list_filter = ('usuario', 'fotografia')
    list_per_page = 10

admin.site.register(Salvas, ListarSalvas)
