from django.contrib import admin
from galeria.models import Fotografia

class ListarFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'clique', 'usuario', 'publicado')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria', 'usuario')
    list_editable = ('publicado', )
    list_per_page = 10


admin.site.register(Fotografia, ListarFotografias)
