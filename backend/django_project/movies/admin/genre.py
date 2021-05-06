"""[summary]

[description]
"""
from django.contrib import admin
from movies.models import GenreModel
from django.utils.translation import ugettext_lazy as _
from project.admin import BaseModelAdmin


@admin.register(GenreModel)
class GenreModelAdmin(BaseModelAdmin):
    save_on_top = True
    list_display = ["name", "created"]
    ordering = ["-created"]
