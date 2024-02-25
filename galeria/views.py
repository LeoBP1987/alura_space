from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia
import random

def index(request):

    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicado=True)

    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    fotografia.clique += 1
    fotografia.save()
    return render(request, 'galeria/imagem.html', {'fotografia' : fotografia})

def buscar(request):
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

