from django.db import models
from django.contrib.auth.models import User

OL_CHOICHES = [
    ('optimist', 'Optimist'),
    ('laser', 'Laser')
]

class Istruttore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        string = self.nome
        string = string[0].upper() + string[1:]
        return string

class Gommone(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        string = self.nome
        string = string[0].upper() + string[1:]
        return string

class Allievo(models.Model):
    nome = models.CharField(max_length=100)
    ol = models.CharField(max_length=100, choices=OL_CHOICHES, default='optimist')

    def __str__(self):
        string = self.nome
        string = string[0].upper() + string[1:]
        return string

class Uscita(models.Model):
    istruttore = models.ForeignKey(Istruttore, on_delete=models.CASCADE)
    gommone = models.ForeignKey(Gommone, on_delete=models.CASCADE)
    allievi = models.ManyToManyField(Allievo)
    data = models.DateField()
    ora_uscita = models.TimeField()
    ora_rientro = models.TimeField()
    ol = models.CharField(max_length=100, choices=OL_CHOICHES, default='optimist')
    