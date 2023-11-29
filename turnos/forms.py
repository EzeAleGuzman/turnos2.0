from django import forms
from .models import Turno

class TurnoForm(forms.ModelForm):  # Use forms.ModelForm instead of just forms
    class Meta:
        model = Turno
        fields = ['nombre','apellido', 'dni', 'medico', 'horario']
        widgets = {'horario': forms.DateTimeInput(attrs={'type': 'datetime-local'})}  # Specify the widget for the 'horario' field
