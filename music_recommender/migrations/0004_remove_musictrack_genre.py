# Generated by Django 5.0.2 on 2024-04-18 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_recommender', '0003_alter_musictrack_artist_alter_musictrack_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musictrack',
            name='genre',
        ),
    ]
