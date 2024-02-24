from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    categorias = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices = categorias, default = '')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='foto/%Y/%m/%d/', blank='True', null='True')
    publicado = models.BooleanField(default='False')
    data_fotografia = models.DateTimeField(default = datetime.now, blank='')

    def __str__(self):
        return self.nome
