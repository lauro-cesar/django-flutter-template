from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    dateCreated = models.DateTimeField(
        auto_now=True, verbose_name=_("Data  de registro")
    )
    lastModified = models.DateTimeField(auto_now=True, verbose_name=_("Último login"))

    @property
    def authToken(self):
        token = None
        try:
            token = Token.objects.get(user=self)
        except Exception:
            pass

        if not token:
            token = Token.objects.create(user=self)
        return token.key

    testUser = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")

    def __str__(self):
        return self.username
