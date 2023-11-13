from django import forms
from .models import Istruttore, Gommone, Allievo, Uscita

class UscitaIstruttoreForm(forms.ModelForm):
    allievi = forms.ModelMultipleChoiceField(queryset=Allievo.objects.none(), widget=forms.CheckboxSelectMultiple())
    """
    data = forms.DateField(
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'class': 'form-control', 
                'placeholder': 'Select a date',
                'type': 'date'
            }
        ),
    )
    """
    ora_rientro = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))  # Usa il widget di tipo ora
    ora_uscita = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))  # Usa il widget di tipo ora

    def clean(self):
        cleaned_data = super().clean()
        ora_rientro = cleaned_data.get('ora_rientro')
        ora_uscita = cleaned_data.get('ora_uscita')

        if ora_rientro and ora_uscita and ora_rientro <= ora_uscita:
            raise forms.ValidationError("L'ora di rientro deve essere successiva all'ora di uscita.")

    class Meta:
        model = Uscita
        fields = ('gommone', 'allievi', 'ora_uscita', 'ora_rientro')

    def __init__(self, user, ol,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["allievi"].queryset = Allievo.objects.filter(ol=ol).order_by('nome')

class UscitaAmministratoreForm(forms.ModelForm):
    allievi = forms.ModelMultipleChoiceField(queryset=Allievo.objects.all().order_by('nome'), widget=forms.CheckboxSelectMultiple())
    data = forms.DateField(
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'class': 'form-control', 
                'placeholder': 'Select a date',
                'type': 'date'
            }
        ),
    )
    ora_rientro = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))  # Usa il widget di tipo ora
    ora_uscita = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))  # Usa il widget di tipo ora

    def clean(self):
        cleaned_data = super().clean()
        ora_rientro = cleaned_data.get('ora_rientro')
        ora_uscita = cleaned_data.get('ora_uscita')

        if ora_rientro and ora_uscita and ora_rientro <= ora_uscita:
            raise forms.ValidationError("L'ora di rientro deve essere successiva all'ora di uscita.")

    class Meta:
        model = Uscita
        fields = ('istruttore', 'gommone', 'allievi', 'data', 'ora_uscita', 'ora_rientro')

    def __init__(self, user, ol, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["allievi"].queryset = Allievo.objects.filter(ol=ol).order_by('nome')
