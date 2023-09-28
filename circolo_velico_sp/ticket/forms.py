from django import forms
from .models import Ticket

class NewTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('user', 'testo',)

class EditTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('stato',)