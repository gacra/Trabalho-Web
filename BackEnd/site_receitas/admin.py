from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Receita)
admin.site.register(Imagem)
admin.site.register(Ingrediente)
admin.site.register(Comentario)
