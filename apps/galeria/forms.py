from django import forms
from apps.galeria.models import Fotografia
from django.contrib.auth.models import User

class FotografiaForms(forms.ModelForm):
    class Meta():
        model = Fotografia
        exclude = ['publicado', 'clique', 'usuario', 'data_fotografia']
        label = {
            'descricao':'Descrição',
            'data_fotografia': 'Data do registro',
            'usuario':'Usuário'
        }

        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control', 'style': 'width: 850px;'}),
            'legenda': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 850px;'}),
            'categoria': forms.Select(attrs={'class':'form-control', 'style': 'width: 200px;'}),
            'descricao': forms.Textarea(attrs={'class':'form-control', 'style': 'width: 850px;'}),
            'foto': forms.FileInput(attrs={'class':'form-control', 'style': 'width: 500px;'}),
            #a data da postagem esta agora carregando a proprio data do dia mantive o código para mérito de consulta
            #'data_fotografia': forms.DateInput(

             #   format = '%d/%m/%Y',
                
              #  attrs={
              # 'type': 'date',
              #  'class': 'form-control',
              #  'style': 'width: 200px;'

            #}),
            
        }

class PorUsuarioForms(forms.ModelForm):
    class Meta():
        model = Fotografia
        exclude = ['nome', 'legenda', 'categoria', 'descricao', 'publicado', 'foto', 'data_fotografia', 'clique']
        label = {
            'usuario':'Usuario'
        }

        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control', 'style': 'width: 200px;'}),
        }
   
    
