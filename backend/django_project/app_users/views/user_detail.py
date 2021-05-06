"""[summary]

[description]

Variables:
    ) {[type]} -- [description]
"""
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.urls import reverse
from app_users.models import AppUserModel


class AppUserDetailView(DetailView):
    """Show the requested book."""

    model = AppUserModel

    def get_object(self, *args, **kwargs):
        return self.model.objects.filter(
            account_id=kwargs.get("account_id", None)
        ).first()

    def dispatch(self, *args, **kwargs):
        if self.get_object() is None:
            return AppUserDetailView.as_view()(request=self.request)
        return super().dispatch(*args, **kwargs)
