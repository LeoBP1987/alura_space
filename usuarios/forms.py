from django import forms

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
        label='Nome Completo',
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