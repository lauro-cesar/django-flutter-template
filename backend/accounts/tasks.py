from celery import shared_task


@shared_task
def clean_temp_users():
    """"""
    print("Cleaning test users")
    pass
