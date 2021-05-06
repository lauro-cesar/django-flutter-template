"""[summary]

[description]
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from project.models import BaseModel, StackedModel


class GenreModel(BaseModel):
    name = models.CharField(max_length=512,verbose_name=_("Titulo"))
    slug = models.SlugField()

    class Meta(BaseModel.Meta):
        verbose_name = _("Genero")
        verbose_name_plural = _("Generos")

    def __str__(self):
        return self.name

