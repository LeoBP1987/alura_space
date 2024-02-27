from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import redirect

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome do Usuario',
        required=True,
        max_length=100,
        widget = forms.TextInput(
                                        attrs={
                                            'class':'form-control',
                                            'placeholder':'Ex.: João Silva'
                                        }
                                    )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=30,
        widget = forms.PasswordInput(
                                        attrs={
                                            'class':'form-control',
                                            'placeholder':'Digite sua senha',
                                        }
                                    )
    )

class CadastrarForms(forms.Form):
    nome_completo = forms.CharField(
        label='Nome para Login',
        required=True,
        max_length=100,
        widget= forms.TextInput(
                                attrs={
                                    'class':'form-control',
                                    'placeholder':'Ex:João Silva',
                                }
                           )
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=70,
        widget= forms.EmailInput(
                                attrs={
                                    'class':'form-control',
                                    'placeholder':'Ex:joao.silva@space.com'
                                }
                           )
    )

    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=30,
        widget = forms.PasswordInput(
                                        attrs={
                                            'class':'form-control',
                                            'placeholder':'Digite sua senha',
                                        }
                                    )
    )

    confirmar_senha = forms.CharField(
        label='Confirmar Senha',
        required=True,
        max_length=30,
        widget = forms.PasswordInput(
                                        attrs={
                                            'class':'form-control',
                                            'placeholder':'Confirme sua senha',
                                        }
                                    )
    )

    def clean_nome_completo(self):
        nome = self.cleaned_data.get('nome_completo')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Não é possível usar espaço no nome de usuário')                                
            elif User.objects.filter(username=nome).exists():
                raise forms.ValidationError('Nome de usuário já utilizado')
            else:
                nome

    def clean_confirmar_senha(self):
        senha = self.cleaned_data.get('senha')
        confirmar_senha = self.cleaned_data.get('confirmar_senha')

        if senha and confirmar_senha:
            if senha != confirmar_senha:
                raise forms.ValidationError('As senhas digitadas não são iguais')
            else:
                return senha