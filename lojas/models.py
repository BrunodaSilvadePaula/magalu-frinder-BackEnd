from django.db import models
from produtos.models import Produto

# Create your models here.

class Loja(models.Model):
    descricao = models.TextField()
    cod_filial = models.IntegerField(null=False, blank=False, unique=True)
    cep = models.CharField(max_length=10)
    produtos = models.ManyToManyField(Produto, blank=True, null=True)

    def __str__(self):
        return 'Filial - ' + str(self.cod_filial)