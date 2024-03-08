from django.contrib import admin
from apps.galeria.models import Fotografia, Likes

class ListarFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'clique', 'usuario', 'publicado')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria', 'usuario')
    list_editable = ('publicado', )
    list_per_page = 10

class ListarLikes(admin.ModelAdmin):
    list_display = ('id', 'fotografia', 'usuario')
    list_display_links = ('id',)
    search_fields = ('usuario', 'fotografia')
    list_filter = ('usuario', 'fotografia')
    list_per_page = 10


admin.site.register(Fotografia, ListarFotografias)
admin.site.register(Likes, ListarLikes)
