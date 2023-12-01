from django import forms
from .models import Turno

class TurnoForm(forms.ModelForm):  # Use forms.ModelForm instead of just forms
    class Meta:
        model = Turno
        fields = ['nombre','apellido', 'dni', 'medico', 'fecha', 'hora']
        widgets = {
        # 'fecha': forms.DateInput(attrs={'type': 'date'}),
        'hora': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),


    }