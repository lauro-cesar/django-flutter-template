from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.views.generic import View
from django.http import JsonResponse
from django.middleware import csrf
from django.core.serializers.json import DjangoJSONEncoder
import json
import re
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from project.permissions import IsOwnerOrReadOnly
import uuid

class Index(View):
    def get(self, request):
        return JsonResponse({'token': '{token}'.format(token=uuid.uuid4().hex)})

    def post(self, request):
        return JsonResponse({'error': 'Please, fill all fields...'})
