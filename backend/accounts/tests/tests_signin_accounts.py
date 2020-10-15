from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
import hashlib
import json
from django.views import View
from django.test import RequestFactory, TestCase, override_settings
from unittest import mock
from django.contrib.auth.models import AnonymousUser
from accounts.views import SignIn, AccountViewSet
from http.cookies import SimpleCookie
from django.http import JsonResponse
from django.http import HttpResponse

from django.forms.models import (
    ModelFormMetaclass,
    construct_instance,
    fields_for_model,
    model_to_dict,
    modelform_factory,
)


User = get_user_model()


class AccountsSigninViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = "demo"
        cls.password = "demo@2020"
        cls.first_name = "First Name"
        cls.last_name = "last name"
        cls.email = "demo@sharedway.app"

    def setUp(self):
        self.factory = RequestFactory()
        self.signin_url = reverse("account-signin")

        self.validUserData = {
            "username": self.username,
            "testUser": True,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }

    def test_signin_negative_invalid_username(self):
        request = self.factory.get(self.signin_url)
        response = SignIn.as_view()(request)

        self.assertEqual(response.status_code, 200)
        body = json.loads(response.content)
        self.assertIsNotNone(body.get("csrftoken", None))
        # headers = {"X-CSRFToken": body.get("csrftoken", None)}

        # form = modelform_factory(User)(self.validUserData)

        # print(form.is_valid())
        # self.assertTrue(form.is_valid())
        # print(form)

        # try:
        #     self.validUserData['username']="0-92"
        #     request = self.factory.post(
        #         self.signin_url,
        #         content_type="application/json",
        #         data=json.dumps(self.validUserData),
        #         **headers,
        #     )
        #     response = SignIn.as_view()(request)
        #     self.assertIsNotNone(response.content)
        #     # j = json.loads(response.content)
        #     self.assertEqual(response.status_code, 403)
        # except Exception as e:
        #     self.fail(e)
