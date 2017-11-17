from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(request):

    form = UsuarioForm()

    return render(request, 'index.html', {'form': form} )

def cadastroUsuario(request):

    return render(request, 'cadastroUsuario.html')

def cadastroReceita(request):

    return render(request, 'cadastroReceita.html')
