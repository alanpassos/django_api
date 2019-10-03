from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=250)
    ativo = models.BooleanField(default=True)
    user = models.OneToOneField(User,  on_delete=models.CASCADE)


    def __str__(self):
        return self.nome

