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

    def create(self, validated_data):
        print(validated_data['ingredientes'])
        receita = Receita.objects.create(
            autor = validated_data['autor'],
            nome_receita = validated_data['nome_receita'],
            descricao = validated_data['descricao'],
            categoria = validated_data['categoria'],
            procoes = validated_data['procoes'],
            val_nutricional = validated_data['val_nutricional'],
            tempo_preparo = validated_data['tempo_preparo'],
            instrucoes_preparo = validated_data['instrucoes_preparo'],
            metodo_cozimento = validated_data['metodo_cozimento'],
            rating = validated_data['rating'],
            num_votos =validated_data['num_votos']
        )



        return receita
