# Generated by Django 3.2 on 2021-05-04 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_settings', '0004_alter_applanguagemodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppLanguageBaseEntryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Data de criação')),
                ('lastModified', models.DateTimeField(auto_now=True, verbose_name='Última modificacao')),
                ('isActive', models.BooleanField(default=True)),
                ('isPublic', models.BooleanField(default=False)),
                ('entry_key', models.CharField(max_length=255, verbose_name='Ident')),
                ('entry_original_value', models.CharField(max_length=255, verbose_name='Ident')),
                ('entry_description', models.CharField(max_length=512, verbose_name='What is it?')),
                ('entry_screenshot', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Optional ScreenShot')),
                ('entry_original_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='app_settings.applanguagemodel')),
            ],
            options={
                'verbose_name': 'Tradução',
                'verbose_name_plural': 'Traduções',
                'ordering': ['created'],
                'abstract': False,
            },
        ),
    ]