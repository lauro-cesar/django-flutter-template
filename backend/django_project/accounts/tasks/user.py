from celery import shared_task
from django.contrib.auth import get_user_model


@shared_task(name="createOrUpdateAppUser", max_retries=3, soft_time_limit=300)
def createOrUpdateAppUser(accountID=None):
    """ """
    User = get_user_model()
    accountUser = User.objects.get(pk=accountID)
    if not isinstance(accountUser, (type(None))):
        accountUser.clientes.update_or_create()


@shared_task(bind=True, name="clean-users", max_retries=3, soft_time_limit=20)
def clean_temp_users(self):
    """ """
    print("Cleaning test users")
