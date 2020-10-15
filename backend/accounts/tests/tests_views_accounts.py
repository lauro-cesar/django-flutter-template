from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ErrorDetail
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
from rest_framework.exceptions import ValidationError

User = get_user_model()


class AccountsViewTests(TestCase):
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
        self.testData = {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
            "username": self.username,
        }

        self.user = User.objects.create_user(
            email=self.email,
            first_name=self.first_name,
            last_name="Last Name",
            username=self.username,
            password=self.password,
        )
        self.token = Token.objects.get(user=self.user)

    def test_json_response(self):
        r = JsonResponse(
            {
                "responseCode": 302,
                "error": "User Exist",
                "success": "error",
                "token": "",
            },
            status=302,
        )
        self.assertEqual(r.status_code, 302)

    def test_username_empty_accounts(self):
        data = self.testData
        data.pop("username")

        request = self.factory.get(self.signin_url)
        request.user = AnonymousUser()
        response = SignIn.as_view()(request)

        self.assertEqual(response.status_code, 200)
        responseBody = json.loads(response.content)
        self.assertIsNotNone(responseBody.get("csrftoken", None))
        headers = {"X-CSRFToken": responseBody.get("csrftoken")}
        request = self.factory.post(
            self.signin_url,
            content_type="application/json",
            data=json.dumps(data),
            **headers,
        )
        signinResponse = SignIn.as_view()(request)
        self.assertEqual(signinResponse.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertJSONEqual(signinResponse.content.decode('utf-8'), {'message':'Please, check username'})

        # self.assertIn('password_mismatch',signinResponseBody.keys())

    def test_email_empty_accounts(self):
        data = self.testData
        data.pop("email")

        request = self.factory.get(self.signin_url)
        request.user = AnonymousUser()
        response = SignIn.as_view()(request)

        self.assertEqual(response.status_code, 200)
        responseBody = json.loads(response.content)
        self.assertIsNotNone(responseBody.get("csrftoken", None))
        headers = {"X-CSRFToken": responseBody.get("csrftoken")}
        request = self.factory.post(
            self.signin_url,
            content_type="application/json",
            data=json.dumps(data),
            **headers,
        )
        signinResponse = SignIn.as_view()(request)
        # signinResponseBody = json.loads(signinResponse.content)
        # print(signinResponseBody)
        self.assertEqual(signinResponse.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertJSONEqual(signinResponse.content.decode('utf-8'), {'message':'Please, check email'})

    def test_first_name_empty_accounts(self):
        data = self.testData
        data.pop("first_name")

        request = self.factory.get(self.signin_url)
        request.user = AnonymousUser()
        response = SignIn.as_view()(request)

        self.assertEqual(response.status_code, 200)
        responseBody = json.loads(response.content)
        self.assertIsNotNone(responseBody.get("csrftoken", None))
        headers = {"X-CSRFToken": responseBody.get("csrftoken")}
        request = self.factory.post(
            self.signin_url,
            content_type="application/json",
            data=json.dumps(data),
            **headers,
        )
        signinResponse = SignIn.as_view()(request)
        # signinResponseBody = json.loads(signinResponse.content)
        # print(signinResponseBody)
        self.assertEqual(signinResponse.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertJSONEqual(signinResponse.content.decode('utf-8'), {'message':'Please, check first_name'})

    def test_last_name_empty_accounts(self):
        data = self.testData
        data.pop("last_name")

        request = self.factory.get(self.signin_url)
        request.user = AnonymousUser()
        response = SignIn.as_view()(request)

        self.assertEqual(response.status_code, 200)
        responseBody = json.loads(response.content)
        self.assertIsNotNone(responseBody.get("csrftoken", None))
        headers = {"X-CSRFToken": responseBody.get("csrftoken")}
        request = self.factory.post(
            self.signin_url,
            content_type="application/json",
            data=json.dumps(data),
            **headers,
        )
        signinResponse = SignIn.as_view()(request)
        # signinResponseBody = json.loads(signinResponse.content)
        # print(signinResponseBody)
        self.assertEqual(signinResponse.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertJSONEqual(signinResponse.content.decode('utf-8'), {'message':'Please, check last_name'})

    def test_done_accounts(self):
        data = self.testData

        request = self.factory.get(self.signin_url)
        request.user = AnonymousUser()
        response = SignIn.as_view()(request)

        self.assertEqual(response.status_code, 200)
        responseBody = json.loads(response.content)
        self.assertIsNotNone(responseBody.get("csrftoken", None))
        headers = {"X-CSRFToken": responseBody.get("csrftoken")}
        request = self.factory.post(
            self.signin_url,
            content_type="application/json",
            data=json.dumps(data),
            **headers,
        )
        signinResponse = SignIn.as_view()(request)
        # signinResponseBody = json.loads(signinResponse.content)
        # print(signinResponseBody)
        self.assertEqual(signinResponse.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertJSONEqual(signinResponse.content.decode('utf-8'), {'message':'Please, check somenthing'})

    def test_password_empty_accounts(self):
        data = {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
        }

        request = self.factory.get(self.signin_url)
        request.user = AnonymousUser()
        response = SignIn.as_view()(request)

        self.assertEqual(response.status_code, 200)
        responseBody = json.loads(response.content)
        self.assertIsNotNone(responseBody.get("csrftoken", None))
        headers = {"X-CSRFToken": responseBody.get("csrftoken")}
        request = self.factory.post(
            self.signin_url,
            content_type="application/json",
            data=json.dumps(data),
            **headers,
        )
        signinResponse = SignIn.as_view()(request)
        # signinResponseBody = json.loads(signinResponse.content)
        # print(signinResponseBody)
        self.assertEqual(signinResponse.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertJSONEqual(signinResponse.content.decode('utf-8'), {'message':'Please, check password'})
