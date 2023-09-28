from django import forms
from .models import Istruttore, Gommone, Allievo, Uscita

class UscitaIstruttoreForm(forms.ModelForm):
    istruttore = forms.ModelChoiceField(queryset=Istruttore.objects.none(), empty_label=None)
    allievi = forms.ModelMultipleChoiceField(queryset=Allievo.objects.all(), widget=forms.CheckboxSelectMultiple())
    data = forms.DateField(widget=forms.SelectDateWidget)  # Usa il widget di tipo data
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

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['istruttore'].queryset = Istruttore.objects.filter(user=user)

class UscitaAmministratoreForm(forms.ModelForm):
    allievi = forms.ModelMultipleChoiceField(queryset=Allievo.objects.all(), widget=forms.CheckboxSelectMultiple())
    data = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))  # Usa il widget di tipo data
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

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
