from django.db import models
from django.utils.translation import ugettext_lazy as _

# Be careful with related_name and related_query_name


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now=True, verbose_name=_("Data de criação"))
    lastModified = models.DateTimeField(
        auto_now=True, verbose_name=_("Última modificacao")
    )
    isActive = models.BooleanField(default=True)
    isPublic = models.BooleanField(default=False)

    @classmethod
    def get_or_none(cls, *args, **kwargs):
        try:
            return cls.objects.get(**kwargs)
        except Exception:
            return None

    class Meta:
        abstract = True
        ordering = ["created"]


class StackedModel(BaseModel):
    stackOrder = models.DecimalField(
        default=100, max_digits=5, decimal_places=2, verbose_name=_("Ordem de exibição")
    )

    class Meta(BaseModel.Meta):
        abstract = True
        ordering = ["created"]
