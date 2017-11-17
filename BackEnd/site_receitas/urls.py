from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'/cadastroUsuario/', views.cadastroUsuario, name="Cadastrar Usuario"),
    url(r'/cadastroReceita/', views.cadastroReceita, name="Cadastrar Receita"),
]
