from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'cadastroUsuario/', views.CadastroUsuario.as_view(), name="Cadastrar Usuario"),
    url(r'cadastroReceitaJson/', views.CadastroReceita.as_view(), name="Cadastrar Receita"),
    url(r'cadastroReceita/', views.cadastroRender, name="TelaCadastrarReceita"),
    url(r'doces/', views.ExibirReceitasDoces.as_view(), name="Doces"),
    url(r'salgados/', views.ExibirReceitasSalgados.as_view(), name="Salgados"),
    url(r'bebidas/', views.ExibirReceitasBebidas.as_view(), name="Bebidas"),
    url(r'xml/(?P<id>\d+)/$', views.detalheReceitaXML, name="xml"),
]
