from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_medicos, name ='medicos'),
    path('crearturno/', views.crear_turno, name= 'crear_turno'),
    path('turnos/', views.ver_turnos, name = 'ver_turnos')
]
