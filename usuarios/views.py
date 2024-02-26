from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastrarForms
from django.contrib.auth.models import User
from django.contrib import auth

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
                return redirect('index')
            else:
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form':form})

def cadastrar(request):
    form=CadastrarForms()

    if request.method == 'POST':
        form = CadastrarForms(request.POST)

        if form.is_valid():
            
            if form['senha'].value() != form['confirmar_senha'].value():
                return redirect('cadastrar')

            nome = form['nome_completo'].value()
            email = form['email'].value()
            senha = form['senha'].value()

            if User.objects.filter(username=nome).exists():
                return redirect('cadastrar')

            usuario = User.objects.create_user(
                                    username=nome,
                                    email=email,
                                    password=senha,
                                )
            
            usuario.save()
            return redirect('login')          
            

    return render(request, 'usuarios/cadastrar.html', {'form':form})
