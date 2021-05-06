"""[summary]

[description]
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from project.models import BaseModel, StackedModel


# this.profile_image,
# this.token,
# this.user_email,
# this.user_id,
# this.user_nicename,
# this.plan,
# this.username,


class AppUserModel(BaseModel):
    @property
    def last_name(self):
        return self.cliente.last_name

    @property
    def first_name(self):
        return self.cliente.first_name

    @property
    def email(self):
        return self.cliente.email

    @property
    def nome(self):
        return self.cliente.get_full_name()

    @property
    def telefone(self):
        return "{ddd} {phone}".format(
            ddd=self.cliente.localAreaCode, phone=self.cliente.phoneNumber
        )

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="clientes",
        verbose_name=_("Usuario"),
    )

    class Meta(BaseModel.Meta):
        verbose_name = _("Registro de cliente")
        verbose_name_plural = _("Registro de clientes")

    def __str__(self):
        return self.nome
