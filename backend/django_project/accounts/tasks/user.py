from celery import shared_task
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
import logging
logger = logging.getLogger(__name__)


User = get_user_model()


@shared_task(name="createOrUpdateAppUser", max_retries=3, soft_time_limit=300)
def createOrUpdateAppUser(accountID=None):
    """ """
    accountUser = User.objects.get(pk=accountID)
    if accountUser:
        accountUser.clientes.update_or_create()


@shared_task(name="createToken", max_retries=3, soft_time_limit=20)
def createToken(self):
    """ """
    accountUser = User.objects.get(pk=accountID)
    if accountUser:
        Token.objects.create(user=instance)
        logger.info("Creating user Token")


@shared_task(bind=True, name="clean-users", max_retries=3, soft_time_limit=20)
def clean_temp_users(self):
    """ """
    logger.info("Cleaning test users")
