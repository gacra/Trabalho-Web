from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(request):

    form = UsuarioForm()

    return render(request, 'index.html', {'form': form} )
