from django.db import models
from django.db.models.fields import EmailField
from django.utils import timezone

# Create your models here.
class Anuncio(models.Model):
    titulo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=9, decimal_places=2)
    empresa = models.CharField(max_length=40)
    descricao = models.TextField(blank=True)
    email = models.CharField(max_length=40)
    novo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.titulo