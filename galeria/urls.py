from django.urls import path
from galeria.views import index, imagem, buscar, buscar_tag

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
    path('buscar_tag/', buscar_tag, name='buscar_tag')
]