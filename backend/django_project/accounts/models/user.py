"""
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django import forms


class User(AbstractUser):
    
    dateCreated = models.DateTimeField(
        auto_now=True, verbose_name=_("Data  de registro")
    )

    lastModified = models.DateTimeField(auto_now=True, verbose_name=_("Último login"))

    profile_image = models.FileField(upload_to="avatars/", default="core/smalllogo.png")

    validEmail = models.BooleanField(default=False)

    countryCode = models.CharField(
        max_length=155, default="55", blank=True, verbose_name=_("Codigo do pais")
    )

    localAreaCode = models.CharField(
        max_length=155, blank=True, default="", verbose_name=_("DDD")
    )

    phoneNumber = models.CharField(
        max_length=155, default="", verbose_name=_("Telefone"), blank=True
    )

    notifications = models.BooleanField(default=True, blank=True)
    news_letter = models.BooleanField(default=True, blank=True)
    sms = models.BooleanField(default=True, blank=True)
    autoAccount = models.BooleanField(default=False, blank=True)
    testUser = models.BooleanField(default=False, blank=True)

    @property
    def notificationToken(self):
        return ""

    @property
    def name(self):
        return self.get_full_name()

    class Meta(AbstractUser.Meta):
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")

    def __str__(self):
        return self.get_full_name()
