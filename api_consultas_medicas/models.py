from django.db import models
from uuid import uuid4

class PessoaProfissional(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255)
    especialidade = models.CharField(max_length=255)
    idade = models.IntegerField()
    data_criacao = models.DateField(auto_now_add=True)

