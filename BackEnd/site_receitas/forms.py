from django.forms import ModelForm
from .models import *

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'nascimento', 'cidade', 'estado', 'telefone', 'usuario')

class IngredienteForm(ModelForm):
    class Meta:
        model = Ingrediente
        fields = ('nome_ingrediente', 'quantidade', 'unidade' )

class ImagemForm(ModelForm):
    class Meta:
        model = Imagem
        fields = ('imagem',)

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
