# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import Http404, HttpResponseRedirect
import json
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

from .models import *
from .serializers import *

# Create your views here.
class Home(APIView):

    renderer_classes = [TemplateHTMLRenderer,]
    template_name = 'index.html'

    def get(self, request, format=None):
        doces = Receita.objects.filter(categoria="d").order_by('-dataCadastro')[:3]
        serielizer_doces = ReceitaSerializer(doces, many=True)
        salgados = Receita.objects.filter(categoria="s").order_by('-dataCadastro')[:3]
        serielizer_salgados = ReceitaSerializer(salgados, many=True)
        bebidas = Receita.objects.filter(categoria="b").order_by('-dataCadastro')[:3]
        serielizer_bebidas = ReceitaSerializer(bebidas, many=True)

        context = {
            'doces': serielizer_doces.data,
            'salgados': serielizer_salgados.data,
            'bebidas': serielizer_bebidas.data
        }
        return Response(context)

class CadastroUsuario(APIView):

    renderer_classes = [TemplateHTMLRenderer,]
    template_name = 'cadastroUsuario.html'

    def get(self, request, format=None):
        return Response({})

    def post(self, request, format=None):
        print(request.data)
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def cadastroRender(request):
    if request.user.is_authenticated:
        return render(request, 'cadastroReceita.html')
    else:
        context = {'errors': 'É necessário entrar para cadastrar uma receita'}
        return render(request, 'entrar.html', context)

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
        doces = Receita.objects.filter(categoria="d").order_by('-dataCadastro')
        serielizer = ReceitaSerializer(doces, many=True)
        print(serielizer.data)
        return Response({'doces': serielizer.data})

class ExibirReceitasSalgados(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'salgados.html'

    def get(self, request, format=None):
        salgados = Receita.objects.filter(categoria="s").order_by('-dataCadastro')
        serializer = ReceitaSerializer(salgados, many=True)
        return Response({'salgados': serializer.data})

class ExibirReceitasBebidas(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bebidas.html'

    def get(self, request, format=None):
        bebidas = Receita.objects.filter(categoria="b").order_by('-dataCadastro')
        serializer = ReceitaSerializer(bebidas, many=True)
        return Response({'bebidas': serializer.data})

def detalheReceita(request, id, tipo = ''):
    try:
        receita = Receita.objects.get(id=id)
    except Receita.DoesNotExist:
        raise Http404
    serializer = ReceitaSerializer(receita)
    if tipo == 'xml':
        return render(request, 'receita.xml', {'receita': serializer.data}, content_type="application/xhtml+xml")
    elif tipo == 'simples':
        return render(request, 'simples.html', {'receita': serializer.data})
    else:
        return render(request, 'detalheReceita.html', {'receita': serializer.data})

def entrar(request):
    if request.method != 'POST':
        context = {'errors': ''}
        return render(request, 'entrar.html', context)
    else:
        username = request.POST['nome_usuario']
        password = request.POST['senha']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('site_receitas:home'))
        else:
            context = {'errors': 'E-mail ou senha incorretos.'}
            return render(request, 'entrar.html', context)

def sair(request):
    logout(request)
    return HttpResponseRedirect(reverse('site_receitas:home'))

class CadastroComentario(APIView):

    def post(self, request, format=None):
        serializer = ComentarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Avaliar(APIView):

    def post(self, request, format=None):
        receita = Receita.objects.get(id = request.data['receita'])
        receita.rating = (receita.rating * receita.num_votos + int(request.data['nota'])) / (receita.num_votos + 1)
        receita.num_votos += 1
        receita.save()
        print("Deu certo!!!")
        return Response({}, status=status.HTTP_201_CREATED)