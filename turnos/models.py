from django.db import models
from datetime import date

class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=45)
    

    def __str__(self):
        return f'{self.nombre}  ({self.especialidad})'
    
  
class Turno(models.Model):
    STATUS_CHOICES = (
        ('E' , 'En Espera'),
        ('P' , 'Atendiendo'),
        ('A' , 'Ausente'),
        ('L', 'Atendido'),
    )
        
    

    nombre = models.CharField( max_length=50, null=True)
    apellido = models.CharField( max_length=50, null=True)
    dni = models.IntegerField(default=0)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today)
    hora = models.TimeField(default='07:00')
    status = models.CharField(max_length=1,choices=STATUS_CHOICES, default='E', verbose_name='estado')
    

    def __str__(self):
        return self.nombre
    
    def marcar_como_atendiendo(self):
        self.status = 'P'  # Cambia el estado a "Atendiendo"
        self.save()

    def marcar_como_ausente(self):
        self.status = 'A'  # Cambia el estado a "Ausente"
        self.save()

    def marcar_como_atendido(self):
        self.status = 'L'  # Cambia el estado a "Atendido"
        self.save()




    
