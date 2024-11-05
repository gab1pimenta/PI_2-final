from django.db import models

# Create your models here.


class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=255)
    usuario = models.CharField(max_length=150, unique=True)
    senha = models.CharField(max_length=128)  # Normalmente, a senha deve ser armazenada como um hash
    funcao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_completo