from django.db import models
from django.contrib.auth.models import User
from apps.galeria.models import Fotografia

class Salvas(models.Model):
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user_fotos'
    )
    fotografia = models.ForeignKey(
        to=Fotografia,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='fotografia'
    )




