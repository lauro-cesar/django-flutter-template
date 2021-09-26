"""from django.views.generic.base import TemplateView

[description]
"""
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.middleware import csrf
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator

from django.views.generic.base import TemplateView
from project.celery import app

class AccountProfile(TemplateView):
    template_name = "profile.html"

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        self.user = self.request.user
        return super().dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "user":self.user
        })
        return context
