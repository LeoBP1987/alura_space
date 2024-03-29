# Generated by Django 5.0.2 on 2024-03-10 14:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('galeria', '0017_delete_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Salvas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotografia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fotografia', to='galeria.fotografia')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_fotos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
