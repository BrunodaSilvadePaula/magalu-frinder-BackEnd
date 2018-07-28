from crypt import methods

from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from lojas.models import Loja
from .serializers import LojaSerializer

class LojaViewSet(ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('produtos__cod_produto', 'produtos__descricao')

    @action(methods=['post'], detail=True)
    def associa_produtos(self, request, pk):
        produtos = request.data['ids']
        loja = Loja.objects.get(pk=pk)
        loja.produtos.set(produtos)
        loja.save()
        return HttpResponse('Ok')