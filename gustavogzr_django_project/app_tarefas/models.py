from django.db import models

# Create your models here.
class responsavel_tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nome
    
class tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=1000, blank=False, null=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao_prevista = models.DateTimeField()
    responsavel = models.ForeignKey(responsavel_tarefa, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo