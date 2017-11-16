from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('nome', 'nascimento', 'cidade', 'estado', 'telefone', 'usuario',)

class IngredienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingrediente
        fields = ('nome_ingrediente',)

class DescricaoReceitaSerielizer(serializers.ModelSerializer):

    class Meta:
        model = DescricaoReceita
        fields = ('nome_usuario', 'nome_receita', 'descricao_receita', 'categoria', 'porcoes', 'calorias', 'tempo_preparo', 'preparo', 'cozimento',)

class ImagemReceitaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImagemReceita
        fields = ('descricao_imagem', 'imagem',)
