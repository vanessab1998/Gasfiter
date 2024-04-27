from pyexpat.errors import messages
from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import render
from django.contrib import messages

from web.forms import ContactForm
from web.models import Servicio

def inicio(request):
    servicios = Servicio.objects.all().filter(is_avaliable=True)
    context = {
        'servicios': servicios,
    }
    return render(request, 'inicio.html', context)

def servicios(request):
    servicios = Servicio.objects.all().filter(is_avaliable=True)
    context = {
        'servicios': servicios,
    }

    return render(request, 'servicios.html', context)


def contacto(request):
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, f' ¡Se ha envíado su mensaje correctamente!')
    return render(request, 'contacto.html', {})

def nosotros(request):
    return render(request, 'nosotros.html', {})

