from django import forms

from .models import Barca, Proprietario, Uscita

class UscitaForm(forms.ModelForm):
    data = forms.DateField(
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'class': 'form-control', 
                'placeholder': 'Select a date',
                'type': 'date'
            }
        ),
    ) # Usa il widget di tipo data

    class Meta():
        model = Uscita
        fields = ('barca', 'persona', 'data', 'rientrato', 'non_socio', 'note')