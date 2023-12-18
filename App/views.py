from django.shortcuts import render, redirect
from django.views import View
from .models import Card, Contact
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request, 'App/inicio.html')

def nosotros(request):
    return render(request, 'App/Nosotros.html')

def servicios(request):
    return render(request, 'App/servicios.html')

def NivelacionEstudios(request):
    return render(request, 'App/sub_paginas/NivelacionEstudios.html')

def ContinuidadEstudios(request):
    return render(request, 'App/sub_paginas/ContinuidadEstudios.html')

def Capacitacion(request):
    return render(request, 'App/sub_paginas/Capacitacion.html')

def ReclutamientoEnLinea(request):
    return render(request, 'App/sub_paginas/ReclutamientoEnLinea.html')

def ValidacionDeEstudios(request):
    return render(request, 'App/sub_paginas/ValidacionDeEstudios.html')

def ArriendoDeMaquinaria(request):
    return render(request, 'App/sub_paginas/ArriendoDeMaquinaria.html')

class CardListView(View):
    def get(self, request):
        cards = Card.objects.all()
        return render(request, 'App/Noticias.html', {'cards': cards})

class AddCardView(View):
    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        Card.objects.create(title=title, description=description)
        return redirect('noticias')

class DeleteCardView(View):
    def post(self, request, id):
        card = Card.objects.get(id=id)
        card.delete()
        return redirect('noticias')
    
def contactanos(request):
   # return render(request, 'App/Contactanos.html')#
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        metodos_contacto = ','.join(request.POST.getlist('contact-methods'))
        servicio_preferido = request.POST.get('servicio-preferido')

        mensaje_contacto = Contact.objects.create(
            rut=rut,
            nombre=nombres,
            apellidos=apellidos,
            email=correo,
            telefono=telefono,
            metodos_contacto=metodos_contacto,
            servicio_preferido=servicio_preferido
        )
        mensaje_contacto.save()
    
        templates = render_to_string('App/sub_paginas/email_contactanos.html', {
            'rut': rut,
            'nombres': nombres,
            'apellidos': apellidos,
            'correo': correo,
            'telefono': telefono,
            'metodos_contacto': metodos_contacto,
            'servicio_preferido': servicio_preferido,
        })

        email = EmailMessage(
            'correo de prueba 5',
            templates,
            settings.EMAIL_HOST_USER,
            ['coriab42@gmail.com']  # Cambia esto al destinatario real
        )

        email.fail_silently = False
        email.send()

        if Contact.objects.filter(rut=rut).exists():
            messages.error(request, 'Ya existe un contacto con este Rut.')
            error_message = 'Ya existe un contacto con este Rut.'
            return redirect('contactanos')

        messages.success(request, 'Se ha enviado correctamente el correo')
        success_message = 'Se ha enviado correctamente el correo'
    return render(request, 'App/Contactanos.html')

        

