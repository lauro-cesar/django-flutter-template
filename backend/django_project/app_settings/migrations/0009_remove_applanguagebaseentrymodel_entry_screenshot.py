# Generated by Django 3.2 on 2021-05-04 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_settings', '0008_auto_20210504_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applanguagebaseentrymodel',
            name='entry_screenshot',
        ),
    ]
