from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager



# Create your models here.

class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100)
    nascimento = models.DateField(null=True, blank=True)
    cidade = models.CharField(max_length=150, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    telefone = models.CharField(max_length=14, null=True ,blank=True)
    usuario = models.EmailField(max_length=50, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['nome']

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome


class DescricaoReceita(models.Model):
    nome_usuario = models.CharField(max_length=100)
    nome_receita = models.CharField(max_length=100)
    descriacao_receita = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    porcoes = models.IntegerField()
    calorias = models.IntegerField()
    tempo_preparo = models.TimeField()
    preparo = models.CharField(max_length=500)
    cozimento = models.CharField(max_length=500)

class Ingrediente(models.Model):
    nome_ingrediente = models.CharField(max_length=100)


class Receita(models.Model):
    fk_descricaoReceita = models.ForeignKey('DescricaoReceita', on_delete=models.CASCADE)
    fk_ingrediente = models.ForeignKey('Ingrediente', on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    unidade = models.CharField(max_length=20)

class ImagemReceita(models.Model):
    fk_descricaoReceita = models.ForeignKey('DescricaoReceita', on_delete=models.CASCADE)
    nome_imagem = models.CharField(max_length=100)
    descricao_imagem = models.CharField(max_length=100)
    imagem = models.ImageField()
