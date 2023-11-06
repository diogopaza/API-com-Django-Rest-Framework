from django.db import models
from uuid import uuid4


class PessoaProfissional(models.Model):   
    nome = models.CharField(max_length=100, null=False, blank=False)
    nome_social = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    celular = models.CharField(max_length=14)
    especialidade = models.CharField(max_length=100)
    idade = models.IntegerField()    
    data_criacao = models.DateField(auto_now_add=True)
    data_nascimento = models.DateField(blank=True, null= True)   

    def __str__(self):
        return self.nome   

class Consulta(models.Model):
    data_consulta = models.DateField(blank=True, null= True) 
    pessoa_profissional = models.ForeignKey(PessoaProfissional, on_delete=models.CASCADE)

    

