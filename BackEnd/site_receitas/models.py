from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager

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

class Receita(models.Model):

    DOCES = "d"
    SALGADOS = "s"
    BEBIDAS = "b"

    ESCOLHA_CATEGORIA = (
        (DOCES, 'Doce'),
        (SALGADOS, 'Salgado'),
        (BEBIDAS, 'Bebidas'),
    )

    dataCadastro = models.DateField(auto_now_add=True, null=True)
    autor = models.CharField(max_length=100, null=True)
    nome_receita = models.CharField(max_length=50, verbose_name="nome da receita", null=True)
    descricao = models.TextField(max_length=300, verbose_name="descrição", null=True)
    #imagems, relação uma para muitos então criou-se a classe imagem e a relação se da pela chave estrangeira fk_receita
    categoria = models.CharField(max_length=1, choices=ESCOLHA_CATEGORIA, default="SC")
    procoes = models.PositiveIntegerField(verbose_name="porções", default=0)
    val_nutricional = models.PositiveIntegerField(verbose_name="valor nutricional", default=0)
    #ingredientes, relação um para muitos, criou-se a classe ingrediente e a relação se da pela chave estrangeira fk_receita
    tempo_preparo = models.PositiveIntegerField(verbose_name="tempo de preparo", default=0)
    instrucoes_preparo = models.TextField(max_length=800, verbose_name="instruções de preparo", null=True)
    metodo_cozimento = models.CharField(max_length=100, verbose_name="método de cozimento", null=True)
    rating = models.PositiveIntegerField(default=0)
    num_votos = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['dataCadastro', '-nome_receita', 'rating']

    def __str__(self):
        return self.nome_receita

    def __unicode__(self):
        return self.nome_receita

class Imagem(models.Model):
    fk_receita_imagem = models.ForeignKey('Receita', related_name='imagens', on_delete=models.CASCADE, default=1)
    imagem = models.ImageField(upload_to="static/images/")

    def __str__(self):
        return str(self.fk_receita_imagem)

    def __unicode__(self):
        return self.fk_receita_imagem

class Ingrediente(models.Model):
    fk_receita_ingrediente = models.ForeignKey('Receita', related_name='ingredientes', on_delete=models.CASCADE, default=0)
    nome_ingrediente = models.CharField(max_length=50, verbose_name="ingrediente")
    quantidade = models.PositiveIntegerField(default=0)
    unidade = models.CharField(max_length=50, default="su")

    def __str__(self):
        return ('%d %s: %s' % (self.quantidade, self.unidade, self.nome_ingrediente))

    def __unicode__(self):
        return ('%d %s: %s' % (self.quantidade, self.unidade, self.nome_ingrediente))

class Comentario(models.Model):
    fk_usuario_comentario = models.ForeignKey('Usuario', related_name="fk_usuario", on_delete=models.CASCADE, default=0)
    fk_receita_comentario = models.ForeignKey('Receita', related_name="comentarios", on_delete=models.CASCADE, default=0)
    texto_comentario = models.TextField(max_length=1000, verbose_name="Comentario")

    def __str__(self):
        return(self.fk_usuario_comentario.nome + " | " + self.fk_receita_comentario.nome_receita)

    def __unicode__(self):
        return(self.fk_usuario_comentario.nome)

    @property
    def nome_usuario(self):
        return self.fk_usuario_comentario.nome
