from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico, Turno
from .forms import TurnoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime

def salir(request):
    logout(request)
    return redirect('/')


def ver_medicos(request):
    medicos = Medico.objects.all()
   
    return render(request, 'medicos.html', {'medicos': medicos})


@login_required
def ver_turnos(request):
    fecha_param = request.GET.get('fecha', None)

    # Obtener todos los turnos o filtrar por fecha
    if fecha_param:
        fecha = datetime.strptime(fecha_param, '%Y-%m-%d').date()
        turnos = Turno.objects.filter(fecha=fecha).order_by('fecha')
    else:
        turnos = Turno.objects.all().order_by('fecha')

    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            # Manejar errores de validación si es necesario
            pass

        # Procesar acciones de cambio de estado
        turno_id = request.POST.get('turno_id')
        accion = request.POST.get('accion')

        if accion == 'atendiendo':
            turno = Turno.objects.get(id=turno_id)
            turno.marcar_como_atendiendo()
        elif accion == 'ausente':
            turno = Turno.objects.get(id=turno_id)
            turno.marcar_como_ausente()
        elif accion == 'atendido':
            turno = Turno.objects.get(id=turno_id)
            turno.marcar_como_atendido()

        return redirect('ver_turnos')
    else:
        form = TurnoForm()

    pertenece_admin = request.user.groups.filter(name='admin').exists()
    pertenece_secretario = request.user.groups.filter(name='secretario').exists()
    return render(request, 'turnos.html', {'turnos': turnos, 'form': form, 'pertenece_admin': pertenece_admin,
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

    return render(request, 'editar_turno.html',  {'form': form, 'turno': turno})



@login_required
def borrar_turno(request, turno_id):
    turno = get_object_or_404(Turno, id=turno_id)
    if request.method == 'POST':
        turno.delete()
    return redirect('ver_turnos')

@login_required
def pacientes_atendidos(request):
    #filtrado de pacientes (todos los atendidos)
    turnos_atendidos = Turno.objects.filter(status='L').order_by('fecha')
    return render(request, 'pacientes_atendidos.html', {'turnos_atendidos': turnos_atendidos})


@login_required
def pacientes_ausentes(request):
    #filtrado de pacientes por ausentes
    turnos_ausentes = Turno.objects.filter(status='A').order_by('fecha')
    return render(request, 'pacientes_ausentes.html', {'turnos_ausentes': turnos_ausentes})