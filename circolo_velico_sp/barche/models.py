from django.db import models

TM_CHOICHES = [
    ('terra', 'Terra'),
    ('mare', 'Mare')
]

class Barca(models.Model):
    nome = models.CharField(max_length=100)
    tm = models.CharField(max_length=100, choices=TM_CHOICHES)

    def __str__(self):
        string = self.nome
        string = string[0].upper() + string[1:]
        return string

class Proprietario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        string = self.nome
        string = string[0].upper() + string[1:]
        return string

class Uscita(models.Model):
    barca = models.ForeignKey(Barca, on_delete=models.CASCADE)
    persona = models.ForeignKey(Proprietario, on_delete=models.CASCADE)
    data = models.DateField()
    tm = models.CharField(max_length=100, choices=TM_CHOICHES, default='terra')
    rientrato = models.BooleanField()
    non_socio = models.BooleanField()
    note = models.CharField(max_length=1000, null=True, blank=True)

    