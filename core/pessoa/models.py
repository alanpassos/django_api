from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=250)
    ativo = models.BooleanField(default=True)


    def __str__(self):
        return self.nome

