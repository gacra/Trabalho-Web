# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.renderers import TemplateHTMLRenderer


from .models import *
from .serializers import *

# Create your views here.
class Home(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request, format=None):
        return Response()


class CadastroUsuario(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cadastroUsuario.html'

    def get(self, request):
        return Response()

    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CadastroReceita(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cadastroReceita.html'

    def get(self, request, format=None):
        return Response()
