from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages
from django.db.models import Max
import random

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicado=True)

    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    fotografia.clique += 1
    fotografia.save()
    return render(request, 'galeria/imagem.html', {'fotografia' : fotografia})

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

    numero_sorteado = random.randint(1, len(fotografias))

    fotografia = get_object_or_404(Fotografia, pk=numero_sorteado)

    return render(request, 'galeria/surpreender.html', {'fotografia':fotografia})

def novas(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicado=True)[:4]
    return render(request, 'galeria/novas.html', {'cards':fotografias})

def mais_vistas(request):
    fotografias = Fotografia.objects.order_by('-clique').filter(publicado=True)[:4]
    return render(request, 'galeria/mais_vistas.html', {'cards':fotografias})

def nova_imagem(request):
    form = FotografiaForms()

    if request.method == 'POST':
        form = FotografiaForms(request.POST)

        if form.is_valid():
            maior_id = Fotografia.objects.aggregate(maior_id=Max('id'))['maior_id']
            id = maior_id + 1
            nome = form['nome'].value()
            legenda = form['legenda'].value()
            categoria = form['categoria'].value()
            descricao = form['descricao'].value()
            foto = form['foto'].value()
            publicado = True
            data = form['data_fotografia'].value()
            usuario = form['usuario'].value()

            foto = Fotografia(id, nome, legenda, categoria, descricao, foto, publicado, data, usuario)

            foto.save()

            messages.success(request, 'Fotografia salva com sucesso')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form':form})

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass

