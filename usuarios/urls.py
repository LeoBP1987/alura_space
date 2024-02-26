from django.urls import path
from usuarios.views import login, cadastrar

urlpatterns = [

    path('login/', login, name='login'),
    path('cadastrar/', cadastrar, name='cadastrar'),
   
]