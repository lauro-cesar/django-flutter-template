from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from project.models import BaseModel, StackedModel


class Model(BaseModel):
    class Meta(BaseModel.Meta):
        verbose_name = _("Name")
        verbose_name_plural = _("Names")

    def __str__(self):
        return self.label
