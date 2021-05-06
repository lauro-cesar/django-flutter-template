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


class AppUserCreateView(CreateView):
    """Create a new book."""

    model = AppUserModel
    fields = ["nome", "email", "telefone", "account_id"]

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, form.instance.nome)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.INFO, "The creation has failed")
        return super().form_invalid(form)
