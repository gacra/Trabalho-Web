from django.forms import ModelForm
from .models import *

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'nascimento', 'cidade', 'estado', 'telefone', 'usuario')

class IngredienteForm(ModelForm):
    class Meta:
        model = Ingrediente
        fields = ('nome_ingrediente', )

class ImagemReceitaForm(ModelForm):
    class Meta:
        model = ImagemReceita
        fields = ('imagem', 'descricao_imagem',)
