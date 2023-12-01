from django.db import models



class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=45)
    

    def __str__(self):
        return f'{self.nombre}  ({self.especialidad})'
    
  
class Turno(models.Model):

    nombre = models.CharField( max_length=50, null=True)
    apellido = models.CharField( max_length=50, null=True)
    dni = models.IntegerField(default=0)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField(default='2023-01-01')
    hora = models.TimeField(default='00:00')
    

    def __str__(self):
        return self.nombre





    
