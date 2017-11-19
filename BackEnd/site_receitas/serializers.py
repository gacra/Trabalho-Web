from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'
        #fields = ('nome_ingrediente', 'quantidade', 'unidade' )

class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        #fields = ('imagem',)
        fields = '__all__'

class ReceitaSerializer(serializers.ModelSerializer):

    imagens = ImagemSerializer(many=True)
    ingredientes = IngredienteSerializer(many=True)

    class Meta:
        model = Receita
        fields = ('dataCadastro',
                  'autor',
                  'nome_receita',
                  'descricao',
                  'imagens',
                  'categoria',
                  'procoes',
                  'val_nutricional',
                  'ingredientes',
                  'tempo_preparo',
                  'instrucoes_preparo',
                  'instrucoes_preparo',
                  'metodo_cozimento',
                  'rating',
                  'num_votos')
