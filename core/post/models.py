from django.db import models
from pessoa.models import Pessoa

class Post(models.Model):
    descricao = models.CharField(max_length=500)
    ativo = models.BooleanField(default=True)
    pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descricao
    
    