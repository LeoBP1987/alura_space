# Generated by Django 5.0.2 on 2024-03-08 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0013_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotografia',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='curtida',
        ),
    ]
