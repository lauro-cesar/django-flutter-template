# Generated by Django 3.2.1 on 2021-05-06 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appsubscriptionplanmodel',
            options={'ordering': ['created'], 'verbose_name': 'Plano de assinatura', 'verbose_name_plural': 'Planos de assinaturas'},
        ),
    ]
