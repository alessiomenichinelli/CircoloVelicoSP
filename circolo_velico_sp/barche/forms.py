from django import forms

from .models import Barca, Proprietario, Uscita

class UscitaForm(forms.ModelForm):
    data = forms.DateField(widget=forms.SelectDateWidget)  # Usa il widget di tipo data

    class Meta():
        model = Uscita
        fields = ('barca', 'persona', 'data', 'rientrato', 'non_socio')