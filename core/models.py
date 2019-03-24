from django.db import models
from django.utils import timezone


class Clientes(models.Model):
    nome = models.CharField(max_length=50, default="Paciente")
    nome_medico = models.CharField(max_length=50, default="Doutor")
    data_consulta = models.DateField(default=timezone.now)
    data_nascimento = models.DateField(default='10/10/1900')
    data_coleta = models.DateField(default=timezone.now)
    
   
    def __str__(self):
        return self.nome
