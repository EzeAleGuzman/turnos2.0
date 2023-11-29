from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.ver_medicos, name ='medicos'),
    path('crearturno/', views.crear_turno, name= 'crear_turno'),
    path('', views.ver_turnos, name = 'ver_turnos')
]
