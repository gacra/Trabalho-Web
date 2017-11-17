from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^cadastroUsuario/', views.CadastroUsuario.as_view(), name="Cadastrar Usuario"),
    url(r'^cadastroReceita/', views.CadastroReceita.as_view(), name="Cadastrar Receita"),
]
