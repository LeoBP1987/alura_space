from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms, PorUsuarioForms
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Max
from datetime import datetime
import random
import os

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicado=True)

    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    fotografia.clique += 1
    fotografia.save()
    foto_usuario = str(fotografia.usuario)
    usuario = request.user.username
    return render(request, 'galeria/imagem.html', {'fotografia' : fotografia, 'usuario' : usuario, 'foto_usuario':foto_usuario})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicado=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {'cards': fotografias})

def buscar_tag(request):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicado=True)

    nome_a_buscar = request.GET['informacao']

    fotografias = fotografias.filter(categoria=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {'cards': fotografias})

def surpreender(request):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicado=True)

    if not fotografias:
        messages.error(request, 'Não há fotografias cadastradas no momento')
        return redirect('index')
    
    foto_id_max = Fotografia.objects.order_by('-id')[0]
    id_max = int(foto_id_max.id)

    numero_sorteado = random.randint(0, id_max)

    while not Fotografia.objects.filter(id=numero_sorteado):
         numero_sorteado = random.randint(0, id_max)

    fotografia = get_object_or_404(Fotografia, pk=numero_sorteado)
    foto_usuario = str(fotografia.usuario)
    usuario = request.user.username

    return render(request, 'galeria/surpreender.html', {'fotografia':fotografia, 'usuario':usuario, 'foto_usuario':foto_usuario})

def novas(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicado=True)[:4]
    return render(request, 'galeria/novas.html', {'cards':fotografias})

def mais_vistas(request):
    fotografias = Fotografia.objects.order_by('-clique').filter(publicado=True)[:4]
    return render(request, 'galeria/mais_vistas.html', {'cards':fotografias})

def minhas_imagens(request):
    usuario_logado = request.user.id
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicado=True, usuario=usuario_logado)

    if not fotografias:
        messages.error(request, f'{request.user.username} não tem fotográfias no momento')
        return redirect('index')

    return render(request, 'galeria/minhas_imagens.html', {'cards':fotografias})

def por_usuario(request):
    form = PorUsuarioForms()
    
    if request.method == 'POST':
        form = PorUsuarioForms(request.POST)
        if form.is_valid():
            nome = form['usuario'].value()
            fotografia = Fotografia.objects.order_by('data_fotografia').filter(publicado=True, usuario=nome)
            return render(request, 'galeria/index.html', {'cards':fotografia})

    return render(request, 'galeria/por_usuario.html', {'form':form})

def nova_imagem(request):
    form = FotografiaForms()

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            fotografia = form.save(commit=False)
            fotografia.usuario = User.objects.get(username=request.user.username)
            fotografia.data_fotografia = datetime.now()
            fotografia.save()
            messages.success(request, 'Fotografia salva com sucesso')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form':form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotogradia Editada com Sucesso')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {'form':form, 'foto_id':foto_id})
    
def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Fotografia Apagada com sucesso')
    return redirect('index')

