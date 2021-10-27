from django.http import response
from django.shortcuts import redirect, render, HttpResponse
from core.models import Evento

# Create your views here.

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    # Filtrar por usuário
    # evento = Evento.objects.filter(usuario=usuario)
    data = {'eventos':evento}
    return render(request, 'agenda.html', data)

def local_evento(request, titulo):
    evento = Evento.objects.get(titulo=titulo)
    return HttpResponse('O local do evento é: {}'.format(evento.local))

# Redireciona para /agenda
# def index(request):
#   return redirect('/agenda/')