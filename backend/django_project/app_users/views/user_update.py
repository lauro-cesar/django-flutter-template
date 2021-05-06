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


class AppUserUpdateView(UpdateView):
    """Update the requested book."""

    model = AppUserModel
    queryset = AppUserModel.objects.all()
    fields = ["nome", "email", "telefone"]

    def get_object(self, *args, **kwargs):
        return self.model.objects.filter(
            account_id=kwargs.get("account_id", None)
        ).first()

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, form.instance.nome)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.INFO, "The update has failed")
        return super().form_invalid(form)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.get_object() is None:
            return BookListView.as_view()(request=self.request)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.add_message(
            self.request, messages.INFO, "The book updated successfully"
        )
        return super().post(request, *args, **kwargs)
