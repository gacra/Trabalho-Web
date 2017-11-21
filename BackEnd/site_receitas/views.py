# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.renderers import TemplateHTMLRenderer, BaseRenderer
from django.http import Http404
import json

from .models import *
from .serializers import *

# Create your views here.
class Home(APIView):

    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'index.html'

    def get(self, request, format=None):
        doces = Receita.objects.filter(categoria="d")[:3]
        serielizer_doces = ReceitaSerializer(doces, many=True)
        salgados = Receita.objects.filter(categoria="s")[:3]
        serielizer_salgados = ReceitaSerializer(salgados, many=True)
        bebidas = Receita.objects.filter(categoria="b")[:3]
        serielizer_bebidas = ReceitaSerializer(bebidas, many=True)

        context = {
            'doces': serielizer_doces.data,
            'salgados': serielizer_salgados.data,
            'bebidas': serielizer_bebidas.data
        }
        return Response(context)

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

def cadastroRender(request):
    return render(request, 'cadastroReceita.html')

class CadastroReceita(APIView):

    def get(self, request, format=None):
        return Response()

    def post(self, request, format=None):
        #print(json.loads(request.data['json_data']))
        serializer = ReceitaSerializer(data=json.loads(request.data['json_data']))
        #serializer = ReceitaSerializer(data=request.data)
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
        print(serielizer.data)
        return Response({'doces': serielizer.data})

class ExibirReceitasSalgados(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'salgados.html'

    def get(self, request, format=None):
        salgados = Receita.objects.filter(categoria="s")
        serializer = ReceitaSerializer(salgados, many=True)
        return Response({'salgados': serializer.data})

class ExibirReceitasBebidas(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bebidas.html'

    def get(self, request, format=None):
        bebidas = Receita.objects.filter(categoria="b")
        serializer = ReceitaSerializer(bebidas, many=True)
        return Response({'bebidas': serializer.data})

def detalheReceitaXML(request, id):
    try:
        receita = Receita.objects.get(id=id)
    except Receita.DoesNotExist:
        raise Http404
    serializer = ReceitaSerializer(receita)
    return render(request, 'receita.xml', {'receita': serializer.data}, content_type="application/xhtml+xml")