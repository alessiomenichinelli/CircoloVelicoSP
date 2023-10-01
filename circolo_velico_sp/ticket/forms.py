from django import forms
from .models import Ticket

class NewTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('testo',)

class EditTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('stato',)