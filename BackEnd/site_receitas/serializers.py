from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome', 'nascimento', 'cidade', 'estado', 'telefone', 'usuario',)

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('nome_ingrediente', 'quantidade', 'unidade' )

class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ('imagem',)
