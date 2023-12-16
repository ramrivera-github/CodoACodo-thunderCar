from django.shortcuts import render
from contacto.models import solenoide

# Create your views here.
def index(request):
    return render(request, "nucleo/index.html")

def quienessomos(request):
    return render(request, "nucleo/quienessomos.html")

def requisitos(request):
    return render(request, "nucleo/requisitos.html")

def nuestraflota(request):
    return render(request, "nucleo/nuestraflota.html")

