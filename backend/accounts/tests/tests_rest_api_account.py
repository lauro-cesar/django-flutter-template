from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
import hashlib
from accounts.serializers import AccountSerializer
from accounts.views import SignIn, AccountViewSet
from rest_framework.renderers import (
    AdminRenderer,
    BaseRenderer,
    BrowsableAPIRenderer,
    DocumentationRenderer,
    HTMLFormRenderer,
    JSONRenderer,
    SchemaJSRenderer,
    StaticHTMLRenderer,
)

User = get_user_model()


class AccountApiTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = "demo"
        cls.password = "demo@2020"
        cls.first_name = "First Name"
        cls.email = "demo@sharedway.app"

    def setUp(self):
        self.user = User.objects.create_user(
            email=self.email,
            first_name=self.first_name,
            last_name="Last Name",
            username=self.username,
            password=self.password,
        )
        self.token = Token.objects.get(user=self.user)
        self.badToken = "sdsds9sidsaaadasdasd6trgasjjsd"

    def test_api_view_set(self):
        headers = {"Authorization": "Bearer {token}".format(token=self.token.key)}
        api_request = APIRequestFactory().get(
            "/rest-api/accounts/{id}.json".format(id=self.user.id),
            format="json",
            **headers,
        )
        api_request.user = self.user
        detail_view = AccountViewSet.as_view({"get": "retrieve"})
        response = detail_view(api_request, pk=self.user.id)
        renderer = JSONRenderer()
        content = renderer.render(response.data, "application/json; indent=2")
        self.assertIsNotNone(content)
        self.assertEqual(response.status_code, 200)

    def test_token_created(self):
        self.assertIsNotNone(self.token)

    def test_account_token_return(self):
        self.assertEqual(self.user.authToken, self.token.key)

    def test_user_default_return(self):
        self.assertEqual(self.user.__str__(), self.username)

    def test_user_serializer_create_positive(self):
        s = AccountSerializer()

        user = s.create(
            validated_data={
                "email": self.email,
                "first_name": self.first_name,
                "last_name": "Last Name",
                "username": "new_user",
                "password": self.password,
            }
        )
        self.assertIsInstance(user, User)

    def test_get_auth_token_negative(self):
        """
        Test for Bad request
        """
        url = reverse("get-token-auth")
        data = {"username": "demo", "password": "Demo"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_auth_token_positive(self):
        """
        Test for user and password correct
        """
        url = reverse("get-token-auth")
        data = {"username": self.username, "password": self.password}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data.get("token"))
