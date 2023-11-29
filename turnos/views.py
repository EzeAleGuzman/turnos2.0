from django.shortcuts import render, redirect
from .models import Medico, Turno
from .forms import TurnoForm

def ver_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos.html', {'medicos': medicos})

def crear_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        form.save()
        return redirect('ver_turnos')

    else:
        form = TurnoForm()

    return render(request, 'crearturno.html', {'form': form})


def ver_turnos(request):
    turnos = Turno.objects.all()
    return render(request, 'turnos.html', {'turnos': turnos})