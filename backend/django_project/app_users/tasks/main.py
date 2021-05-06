from celery import shared_task
from django.conf import settings
import random
import requests
import base64
from django.utils.encoding import smart_str,smart_text
from django.core.cache import cache
from django.utils.text import slugify
import traceback
import time


@shared_task
def mainTask():
    pass
