# Generated by Django 3.2 on 2021-05-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='genres',
            field=models.ManyToManyField(to='movies.GenreModel'),
        ),
    ]
