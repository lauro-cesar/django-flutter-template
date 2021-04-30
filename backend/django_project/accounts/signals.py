from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from celery import shared_task
from project.celery import app
