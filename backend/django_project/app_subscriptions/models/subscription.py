""" [summary]

[description]
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from project.models import BaseModel, StackedModel


class AppSubscriptionPlanModel(BaseModel):
    label = models.CharField(max_length=256,verbose_name=_("Nome do plano"))
    description = models.TextField(verbose_name=_("Descrição do plano"))

    plan_price = models.DecimalField(default=00000, decimal_places=2, max_digits=8,verbose_name=_("Valor do plano"))

    due_on_day_of_the_month = models.SmallIntegerField(
       verbose_name=_("Dia do vencimento"))
    invoince_on_day_of_the_month = models.SmallIntegerField(
       verbose_name=_("Dia do envio da fatura"))


    class Meta(BaseModel.Meta):
        verbose_name = _("Plano de assinatura")
        verbose_name_plural = _("Planos de assinaturas")

    def __str__(self):
        return self.label
