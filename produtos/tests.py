from django.test import TestCase
from .models import Produto
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from produtos.api.viewsets import ProdutoViewSet

# Create your tests here.

class TesteProdutoViewSet(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user('userrootproduct', None, 'testedeuser_')
        Token.objects.create(user=self.user)

        self.loja = Produto.objects.create(cod_produto='1234', descricao='melhor do mercado',
                                        valor_venda='300.00')

        self.view_list = ProdutoViewSet.as_view({'get': 'list'})
        self.view_retrieve = ProdutoViewSet.as_view({'get': 'retrieve'})
        self.view_create = ProdutoViewSet.as_view({'post': 'create'})
        self.view_delete = ProdutoViewSet.as_view({'delete': 'destroy'})
        self.view_update = ProdutoViewSet.as_view({'put': 'update'})

        token = Token.objects.get(user__username='userrootproduct')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.data_success = {'cod_produto': '12345', 'descricao': 'melhor do mercado',
                             'valor_venda': 300}
        self.data_failure = {'cod_produto': '123456', 'valor_venda': 300.00}
        self.data_update = {'cod_produto': '9876', 'descricao': 'melhor do mercado',
                            'valor_venda': 350.00}

    def test_produto_view_success_status_code(self):
        url = '/produto'
        request = self.factory.get(url)
        response = self.view_list(request)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_produto_post_success_status_code(self):
        url = '/produto'
        request = self.factory.post(url, self.data_success)
        force_authenticate(request, user=self.user)
        response = self.view_create(request)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_produto_post_unauthorized_status_code(self):
        url = '/produto'
        request = self.factory.post(url, self.data_success)
        response = self.view_create(request)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_produto_post_failure_status_code(self):
        url = '/produto'
        request = self.factory.post(url, self.data_failure)
        force_authenticate(request, user=self.user)
        response = self.view_create(request)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_produto_put_success_status_code(self):
    #     url = '/loja/' + str(self.loja.pk) + '/'
    #     request = self.factory.put(url, self.data_update)
    #     force_authenticate(request, user=self.user)
    #     response = self.view_update(request)
    #     self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
