from crypt import methods
from rest_framework.response import Response
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from operator import itemgetter
import urllib.request, json
from lojas.models import Loja
from produtos.models import Produto
from .serializers import LojaSerializer

class LojaViewSet(ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('produtos__cod_produto', 'produtos__descricao')


    @action(methods=['get'], detail=False)
    def busca_produtos(self, request):
        try:
            cep = request.query_params.get('cep', None)
            produto = request.query_params.get('produto', None)

            if((cep is not None) and (produto is not None)):
                query_filial = Loja.objects.filter(produtos__cod_produto__iexact=produto)
                if query_filial.count() == 0:
                    query_filial = Loja.objects.filter(produtos__descricao__iexact=produto)
                    if query_filial.count() > 0:
                        retorno = self.monta_retorno(query_filial, produto, cep)
                    else:
                        return Response({'error': 'Não foi encontrado resultado para sua pesquisa'},
                                        status=status.HTTP_204_NO_CONTENT)
                else:
                    retorno = self.monta_retorno(query_filial, produto, cep)

                if retorno is None:
                    return Response({'error': 'Não encontramos o seu Cep'},
                                status=status.HTTP_204_NO_CONTENT)
                return Response({
                    'retorno': retorno
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'O produto e o Cep são necessarios para a busca'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'verifique os parametros que esta enviando'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def associa_produtos(self, request, pk):
        produtos = request.data['ids']
        loja = Loja.objects.get(pk=pk)
        loja.produtos.clear()
        loja.produtos.set(produtos)
        loja.save()
        return HttpResponse('Ok')

    def get_distancia(self, cep_cliente, cep_filial):
        try:
            with urllib.request.urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+cep_cliente+"&destinations="+cep_filial+"&key=AIzaSyCNYYmdp4JklOFyD-F00WynrS6po0-rK7U") as url:
                retorno = json.loads(url.read().decode())
            for data in retorno['rows']:
                for element in data['elements']:
                    distancia_km = str(round(element['distance']['value'] / 1000, 0)) + ' Km'
            return distancia_km
        except:
            return None

    def get_produto(self, produto):
        query_produto = Produto.objects.filter(cod_produto__iexact=produto)
        if query_produto.count() > 0:
            query_produto = Produto.objects.filter(descricao__iexact=produto)
            vlr_produto = query_produto[0].valor_venda
        else:
            query_produto = Produto.objects.filter(descricao__iexact=produto)
            vlr_produto = query_produto[0].valor_venda
        return vlr_produto

    def monta_retorno(self, filiais, produto,cep):
        retorno = []
        for filial in filiais:
            distance = self.get_distancia(cep, filial.cep)
            if distance is None:
                return None

            obj = {
                "descricao": filial.descricao,
                "filial": filial.cod_filial,
                "cep": filial.cep,
                "vlr_produto": self.get_produto(produto),
                "distancia": self.get_distancia(cep, filial.cep)
            }
            retorno.append(obj)
        retorno = sorted(retorno, key =lambda x: x['distancia'])
        return retorno
