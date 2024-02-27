from django.urls import path
from usuarios.views import login, cadastrar,logout

urlpatterns = [

    path('login/', login, name='login'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('logout/', logout, name='logout')
   
]