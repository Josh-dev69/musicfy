# Generated by Django 5.0.2 on 2024-04-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('tempo', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Music Tracks',
            },
        ),
    ]
