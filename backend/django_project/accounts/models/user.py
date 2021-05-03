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

    class Meta(AbstractUser.Meta):
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")

    def __str__(self):
        return self.get_full_name()
