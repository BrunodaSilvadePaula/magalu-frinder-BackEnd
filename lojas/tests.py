from django.test import TestCase, RequestFactory
from .models import Loja
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from lojas.api.viewsets import LojaViewSet

# Create your tests here.

class TesteLojaViewSet(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user('userroot', None, 'testedeuser_')
        Token.objects.create(user=self.user)

        self.loja = Loja.objects.create(descricao='cadastro teste', cod_filial='765',
                                        cep='1440088')

        self.view_list = LojaViewSet.as_view({'get': 'list'})
        self.view_retrieve = LojaViewSet.as_view({'get': 'retrieve'})
        self.view_create = LojaViewSet.as_view({'post': 'create'})
        self.view_delete = LojaViewSet.as_view({'delete': 'destroy'})
        self.view_update = LojaViewSet.as_view({'put': 'update'})

        token = Token.objects.get(user__username='userroot')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.data_success = {'descricao': 'loja teste', 'cod_filial': '0987', 'cep': '14406269'}
        self.data_failure = {'descricao': 'loja teste', 'cep': '14406269'}
        self.data_update = {'descricao': 'update teste', 'cod_filial': '765', 'cep': '1440088'}

    def test_loja_view_success_status_code(self):
        url = '/loja'
        request = self.factory.get(url)
        response = self.view_list(request)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_loja_post_success_status_code(self):
        url = '/loja'
        request = self.factory.post(url, self.data_success)
        force_authenticate(request, user=self.user)
        response = self.view_create(request)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_loja_post_unauthorized_status_code(self):
        url = '/loja'
        request = self.factory.post(url, self.data_success)
        response = self.view_create(request)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_loja_post_failure_status_code(self):
        url = '/loja'
        request = self.factory.post(url, self.data_failure)
        force_authenticate(request, user=self.user)
        response = self.view_create(request)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_loja_put_success_status_code(self):
    #     url = '/loja/' + str(self.loja.pk) + '/'
    #     print(url)
    #     request = self.factory.put(url, self.data_update)
    #     force_authenticate(request, user=self.user)
    #     response = self.view_update(request)
    #     self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)