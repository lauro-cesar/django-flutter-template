# Generated by Django 3.2 on 2021-05-06 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_notifications", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="appnotificationmodel",
            old_name="processed",
            new_name="isProcessed",
        ),
    ]
