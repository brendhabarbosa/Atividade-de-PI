from django.db import models

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    celular = models.CharField(max_length=15)
class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    carga_horaria = models.IntegerField()
    codigo = models.CharField(max_length=200)
