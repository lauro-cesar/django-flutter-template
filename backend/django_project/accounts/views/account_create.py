from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from project.authentication import APITokenAuthentication
from django.views.generic import View
from django.http import JsonResponse
from django.middleware import csrf
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
import json
import re


User = get_user_model()

# User._meta.get_field('email')._unique = True


class AccountCreate(View):
    def get(self, request):
        return JsonResponse({"csrftoken": "%s" % csrf.get_token(request)}, status=200)

    def post(self, request):
        checkList = []
        body = json.loads(request.body)
        fullName = body.get("fullname", "Nome completo")
        firstName = " ".join(fullName.split()[0:-1])
        lastName = " ".join(fullName.split()[-1:])
        email = body.get("email", False)
        checkList.append(email)
        password = body.get("password", False)
        checkList.append(password)
        password_check = body.get("password_check", False)
        checkList.append(password_check)
        if False not in checkList:
            mail = email.strip().lower()
            params = {}
            params.update(
                {
                    "username": mail,
                    "email": mail,
                    "first_name": firstName,
                    "last_name": lastName,
                    "password": password.strip()
                }
            )
            try:
                u = User.objects.create_user(mail,mail,password.strip())                               
                u.last_name = lastName
                u.first_name = firstName
                u.testUser = body.get("testUser", False)
                u.save()
                return JsonResponse(
                    {"id": u.pk, "token": u.authToken},
                    status=201,
                )

            except Exception as e:
                print(e.__repr__())
                fields = {
                    "password": "Please, check password",
                    "email": "Uma conta com o email informado existe!",
                    "first_name": "Please, check first_name",
                    "last_name": "Please, check last_name",
                    "username": "Uma conta com o email informado existe!",
                }
                if isinstance(e, (IntegrityError)):
                    return JsonResponse(
                        {"message": "Uma conta com o email informado existe!"},
                        status=400,
                    )
                if isinstance(e, (ValidationError)):
                    for k, v in e.error_dict.items():
                        if k in fields.keys():
                            return JsonResponse({"message": fields[k]}, status=400)


                return JsonResponse({"message": "error unknow"}, status=422)

        


        return JsonResponse({"message": "Error"}, status=400)
