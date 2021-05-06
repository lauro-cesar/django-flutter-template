"""[summary]

[description]
"""
from django.contrib import admin
from movies.models import MovieModel
from django.utils.translation import ugettext_lazy as _
from project.admin import BaseModelAdmin


@admin.register(MovieModel)
class MovieModelAdmin(BaseModelAdmin):
    save_on_top = True
    list_display = ["title", "created"]
    ordering = ["-created"]
