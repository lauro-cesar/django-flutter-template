# Generated by Django 3.2 on 2021-05-04 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_settings', '0005_applanguagebaseentrymodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applanguagemodel',
            options={'ordering': ['created'], 'verbose_name': 'Idioma', 'verbose_name_plural': 'Idiomas'},
        ),
    ]
