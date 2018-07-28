from rest_framework.serializers import ModelSerializer
from lojas.models import Loja

class LojaSerializer(ModelSerializer):
    class Meta:
        model = Loja
        fields = ('id', 'descricao', 'cod_filial', 'cep')