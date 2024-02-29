from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastrarForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():

            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha,
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso.')
                return redirect('index')
            else:
                messages.error(request, 'Nome de usuário ou senha não conferem.')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form':form})

def cadastrar(request):
    form=CadastrarForms()

    if request.method == 'POST':
        form = CadastrarForms(request.POST)

        if form.is_valid():
            
            nome = form['nome_completo'].value()
            email = form['email'].value()
            senha = form['senha'].value()

            usuario = User.objects.create_user(
                                    username=nome,
                                    email=email,
                                    password=senha,
                                )
            
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('login')          
            

    return render(request, 'usuarios/cadastrar.html', {'form':form})

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request,'Logout Efetuado com Sucesso')
    else:
        auth.logout(request)
    return redirect('login')
