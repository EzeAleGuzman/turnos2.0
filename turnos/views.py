from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico, Turno
from .forms import TurnoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

def salir(request):
    logout(request)
    return redirect('/')


def ver_medicos(request):
    medicos = Medico.objects.all()
   
    return render(request, 'medicos.html', {'medicos': medicos})


@login_required
def ver_turnos(request):
    turnos = Turno.objects.all().order_by('fecha')
    
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        form.save()
        return redirect('ver_turnos')

    else:
        form = TurnoForm()
    pertenece_admin = request.user.groups.filter(name='admin').exists()
    pertenece_secretario = request.user.groups.filter(name='secretario').exists()    
    return render(request, 'turnos.html', {'turnos': turnos, 'form': form,'pertenece_admin': pertenece_admin,
        'pertenece_secretario': pertenece_secretario})


def editar_turno(request, turno_id):
    turno = get_object_or_404(Turno, id=turno_id)

    if request.method == 'POST':
        form = TurnoForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
            return redirect('ver_turnos')
    else:
        form = TurnoForm(instance=turno)

    return render(request, 'editar_turno.html', {'form': form})

@login_required
def borrar_turno(request, turno_id):
    turno = get_object_or_404(Turno, id=turno_id)
    if request.method == 'POST':
        turno.delete()
    return redirect('ver_turnos')