# Generated by Django 3.2 on 2021-05-04 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_settings', '0010_auto_20210504_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applanguageentrykeymodel',
            name='entry_key',
            field=models.CharField(help_text='Deixe em branco para auto criar', max_length=255, verbose_name='ID único'),
        ),
    ]