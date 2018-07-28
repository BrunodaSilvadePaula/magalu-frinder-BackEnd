from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from produtos.models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('cod_produto', 'descricao')