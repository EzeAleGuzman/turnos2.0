from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.ver_medicos, name ='medicos'),
    # path('crearturno/', views.crear_turno, name= 'crear_turno'),
    path('editar_turno/<int:turno_id>/', views.editar_turno, name='editar_turno'),
    path('borrar_turno/<int:turno_id>/', views.borrar_turno, name='borrar_turno'),
    path("salir/", views.salir, name="salir"),
    path('', views.ver_turnos, name = 'ver_turnos'),
]
