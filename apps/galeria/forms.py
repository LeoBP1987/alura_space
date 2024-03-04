from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta():
        model = Fotografia
        exclude = ['publicado', 'clique']
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
            'data_fotografia': forms.DateInput(

                format = '%d/%m/%Y',
                
                attrs={
                'type': 'date',
                'class': 'form-control',
                'style': 'width: 200px;'

            }),
            'usuario': forms.Select(attrs={'class': 'form-control', 'style': 'width: 200px;'}),
        }

