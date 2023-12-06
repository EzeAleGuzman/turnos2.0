from django import forms
from .models import Turno


class DDMMYYYYDateInput(forms.DateInput):
    input_type = 'text'

    def __init__(self, attrs=None, format='%d/%m/%Y'):
        default_attrs = {'pattern': '\d{2}/\d{2}/\d{4}', 'title': 'Formato requerido: dd/mm/yyyy'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs, format=format)



class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['nombre', 'apellido', 'dni', 'medico', 'fecha', 'hora']
        widgets = {
            'fecha': DDMMYYYYDateInput(attrs={'class': 'datepicker'}),
            'hora': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }

