# Generated by Django 5.0.2 on 2024-04-16 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_recommender', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musictrack',
            name='tempo',
        ),
    ]
