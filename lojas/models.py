from django.db import models

# Create your models here.

class Loja(models.Model):
    descricao = models.TextField()
    cod_filial = models.IntegerField(null=True, blank=True)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return 'Filial - ' + str(self.cod_filial)