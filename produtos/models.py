from django.db import models

# Create your models here.

class Produto(models.Model):
    cod_produto = models.CharField(max_length=15, unique=True)
    descricao = models.TextField()
    valor_venda = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.cod_produto + ' - ' + self.descricao