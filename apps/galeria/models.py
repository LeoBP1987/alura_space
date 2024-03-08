from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Fotografia(models.Model):

    categorias = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')
    ]

    nome = models.CharField(max_length=70, null=False, blank=False)
    legenda = models.CharField(max_length=80, null=False, blank=False)
    categoria = models.CharField(max_length=50, choices = categorias, default = '')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='foto/%Y/%m/%d/', blank='True', null='True')
    publicado = models.BooleanField(default='True')
    data_fotografia = models.DateTimeField(default = datetime.now, blank='')
    clique = models.IntegerField(default=0)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.nome

class Likes(models.Model):
    fotografia = models.ForeignKey(
        to=Fotografia,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='fotografia'            
        )
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user_like'
        )
    
