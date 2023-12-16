from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Contacto
from django.shortcuts import get_object_or_404

# Create your views here.
#def contacto(request):
#    return render(request, "contacto/contacto.html")

def listado(request): 
    contactos = Contacto.objects.all()
    return render(request, "contacto/listado.html", {'contactos' : contactos})
    
@csrf_protect
def contacto(request):
    if request.method == "POST":
        apellido = request.POST.get('apellido')
        nombre = request.POST.get('nombre')
        dni = request.POST.get('dni')
        fecNac = request.POST.get('fecNac')
        email = request.POST.get('email')
        adjuntar = request.FILES.get('adjuntar')
        consulta = request.POST.get('consulta')
        infocontacto = Contacto(apellido=apellido, nombre=nombre, dni=dni, fecNac=fecNac, email=email, adjuntar=adjuntar, consulta=consulta)
        infocontacto.save()
        return render(request, 'nucleo/index.html')
    else:
        return render(request, "contacto/contacto.html")
    #return render(request, 'nucleo/requisitos.html')
    
def delete(request, pk):
    borrar = get_object_or_404(Contacto, id=pk)
    borrar.delete()
    contactos = Contacto.objects.all()
    return render(request, "contacto/listado.html", {'contactos' : contactos})