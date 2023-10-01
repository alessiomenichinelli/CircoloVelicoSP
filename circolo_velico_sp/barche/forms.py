from django import forms

from .models import Barca, Proprietario, Uscita

class UscitaForm(forms.ModelForm):
    barca = forms.ModelChoiceField(queryset=Barca.objects.none(), empty_label=None)
    persona = forms.ModelChoiceField(queryset=Proprietario.objects.none(), empty_label=None)
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


    def __init__(self, tm, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["barca"].queryset = Barca.objects.filter(tm=tm).order_by('nome')
        self.fields["persona"].queryset = Proprietario.objects.all().order_by('nome')