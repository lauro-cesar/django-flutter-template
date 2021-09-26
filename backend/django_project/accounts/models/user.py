"""
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    TASKS={
        'on_create':['addUserToDefaultTrial','createToken'],
        'on_save':[],
        'on_delete':['removeUserFromStripe']
    }
    dateCreated = models.DateTimeField(auto_now=True)
    lastModified = models.DateTimeField(auto_now=True)
    testUser = models.BooleanField(default=False)
    guestUser = models.BooleanField(default=False)
    validEmail = models.BooleanField(default=False)
    email = models.EmailField(unique=True)

    def generateSingleSigninToken(self):
        token = default_token_generator.make_token(self)
        uidb64 = urlsafe_base64_encode(str(self.pk).encode())
        return {"token": token, "uidb64": uidb64}


    @property
    def name(self):
        return self.get_full_name()

    class Meta(AbstractUser.Meta):
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")

    def __str__(self):
        return self.get_full_name()
