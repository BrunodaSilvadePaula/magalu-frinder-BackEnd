from rest_framework.serializers import ModelSerializer
from lojas.models import Loja
from produtos.api.serializers import ProdutoSerializer

class LojaSerializer(ModelSerializer):
    produtos = ProdutoSerializer(many=True, read_only=True)

    class Meta:
        model = Loja
        fields = ('id', 'descricao', 'cod_filial', 'cep', 'produtos')