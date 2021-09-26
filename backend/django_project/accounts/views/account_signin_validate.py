"""[summary]

[description]
"""
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.tokens import default_token_generator

from django.utils.http import (
    url_has_allowed_host_and_scheme,
    urlsafe_base64_decode,
)


from django.views.generic.base import TemplateView
from django.contrib.auth import (
    REDIRECT_FIELD_NAME,
    get_user_model,
    update_session_auth_hash,
)

UserModel = get_user_model()


class AccountSigninValidate(TemplateView):
    template_name = "account_signin_validate.html"
    success_url = reverse_lazy("account-profile")
    token_generator = default_token_generator

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            UserModel.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        assert "uidb64" in kwargs and "token" in kwargs
        self.user = self.get_user(kwargs["uidb64"])

        if self.user is not None:
            token = kwargs["token"]
            if self.token_generator.check_token(self.user, token):
                self.user.validEmail = True
                self.user.save()
        HttpResponseRedirect(self.success_url)
