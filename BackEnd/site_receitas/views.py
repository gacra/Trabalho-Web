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

    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'index.html'

    #def get(self, request, format=None):
    #    receitas = Receita.objects.all().order_by('dataCadastro')
    #    serializer = ReceitaSerializer(receitas, many=True)
    #    return Response(serializer.data)

    def get(self, request, format=None):
        receitas = Receita.objects.all().order_by('dataCadastro', '-categoria')
        serializer = ReceitaSerializer(receitas, many=True)
        return Response({'receitas': serializer.data})



class CadastroUsuario(APIView):

    renderer_classes = (TemplateHTMLRenderer)
    template_name = 'cadastroUsuario.html'

    def get(self, request, format=None):
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

    def post(self, request, format=None):
        serializer = ReceitaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExibirReceitasDoces(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'doces.html'

    def get(self, request, format=None):
        doces = Receita.objects.filter(categoria="d")
        serielizer = ReceitaSerializer(doces, many=True)
        return Response({'doces': serielizer.data})

class ExibirReceitasSalgados(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'salgados.html'

    def get(self, request, format=None):
        salgados = Receita.objects.filter(categoria="s")
        serializer = ReceitaSerializer(salgados, many=True)
        return Response({'salgados': serielizer.data})

class ExibirReceitasBebidas(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bebidas.html'

    def get(self, request, format=None):
        bebidas = Receita.objects.filter(categoria="b")
        serializer = ReceitaSerializer(bebidas, many=True)
        return Response({'bebidas': serielizer.data})
