from django.db import models
from django.contrib.auth.models import User


STATO_TICKET = [
    ('Inviato', 'Inviato'),
    ('In elaborazione', 'In elaborazione'),
    ('Risolto', 'Risolto')
]

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testo = models.CharField(max_length=500)
    stato = models.CharField(max_length=50, choices=STATO_TICKET)
