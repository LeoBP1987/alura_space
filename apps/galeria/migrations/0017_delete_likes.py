# Generated by Django 5.0.2 on 2024-03-09 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0016_alter_fotografia_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Likes',
        ),
    ]