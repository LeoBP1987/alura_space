from django.urls import path
from apps.galeria.views import \
    index, imagem, buscar, buscar_tag, surpreender, novas, mais_vistas, \
        nova_imagem, editar_imagem, deletar_imagem, minhas_imagens, \
        por_usuario, conta_likes

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
    path('buscar-tag/', buscar_tag, name='buscar_tag'),
    path('surpreender/', surpreender, name='surpreender'),
    path('novas/', novas, name='novas'),
    path('mais-vistas/', mais_vistas, name='mais_vistas'),
    path('nova-imagem/', nova_imagem, name='nova_imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('deletar-imagem/<int:foto_id>', deletar_imagem, name='deletar_imagem'),
    path('minhas-imagens/', minhas_imagens, name='minhas_imagens'),
    path('por-usuario/', por_usuario, name='por_usuario'),
    path('conta-likes/<int:foto_id>', conta_likes, name='conta_likes')
]