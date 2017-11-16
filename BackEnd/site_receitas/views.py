from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    form = UsuarioForm()

    return render(request, 'index.html', {'form': form} )
