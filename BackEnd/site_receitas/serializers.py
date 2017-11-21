from rest_framework import serializers
from .models import *
from drf_base64.serializers import ModelSerializer as ModelSerializer64

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        usuario = Usuario.objects.create_user(
            password=validated_data['password'],
            nome=validated_data['nome'],
            usuario=validated_data['usuario']
        )

        return usuario

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'
        #fields = ('nome_ingrediente', 'quantidade', 'unidade' )

class ImagemSerializer(ModelSerializer64):
    class Meta:
        model = Imagem
        #fields = ('imagem',)
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('fk_usuario_comentario', 'fk_receita_comentario', 'texto_comentario', 'nome_usuario')
        read_only_fields = ('nome_usuario',)

class ReceitaSerializer(serializers.ModelSerializer):

    imagens = ImagemSerializer(many=True)
    ingredientes = IngredienteSerializer(many=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)

    class Meta:
        model = Receita
        fields = ('id',
                  'dataCadastro',
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
                  'num_votos',
                  'comentarios',)

    def create(self, validated_data):

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

        ingredientes_json = validated_data['ingredientes']

        for ingrediente_json in ingredientes_json:

            ingrediente = Ingrediente.objects.create(
                nome_ingrediente = ingrediente_json['nome_ingrediente'],
                quantidade = ingrediente_json['quantidade'],
                unidade = ingrediente_json['unidade'],
                fk_receita_ingrediente = receita
            )

        imagem_json = {'imagem':validated_data['imagens'][0]['imagem'], 'fk_receita_imagem': receita.id}

        serializer = ImagemSerializer(data=imagem_json)
        if serializer.is_valid():
            serializer.save()
        #print(serializer.errors)

        return receita
