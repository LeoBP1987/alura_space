from django.urls import path
from galeria.views import index, imagem, buscar, buscar_tag, surpreender, novas, mais_vistas

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
    path('buscar_tag/', buscar_tag, name='buscar_tag'),
    path('supreender/', surpreender, name='surpreender'),
    path('novas/', novas, name='novas'),
    path('mais_vistas/', mais_vistas, name='mais_vistas')
]