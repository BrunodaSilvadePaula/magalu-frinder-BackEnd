from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from usuarios.api.viewsets import UsuarioViewSet

# Create your tests here.

class TesteUsuarioViewSet(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user('userrootusuario', None, 'testedeuser_')
        Token.objects.create(user=self.user)

        self.view_list = UsuarioViewSet.as_view({'get': 'list'})
        self.view_retrieve = UsuarioViewSet.as_view({'get': 'retrieve'})
        self.view_create = UsuarioViewSet.as_view({'post': 'create'})
        self.view_delete = UsuarioViewSet.as_view({'delete': 'destroy'})
        self.view_update = UsuarioViewSet.as_view({'put': 'update'})

        token = Token.objects.get(user__username='userrootusuario')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.data_success = {'username': 'cadastroteste', 'password': 'senhaparaacesso'}
        self.data_failure = {'usuario': 'cadastroteste'}

    def test_usuario_view_success_status_code(self):
        url = '/usuario'
        request = self.factory.get(url)
        response = self.view_list(request)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_usuario_post_success_status_code(self):
        url = '/usuario'
        request = self.factory.post(url, self.data_success)
        force_authenticate(request, user=self.user)
        response = self.view_create(request)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_usuario_post_unauthorized_status_code(self):
        url = '/usuario'
        request = self.factory.post(url, self.data_success)
        response = self.view_create(request)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_usuario_post_failure_status_code(self):
        url = '/usuario'
        request = self.factory.post(url, self.data_failure)
        force_authenticate(request, user=self.user)
        response = self.view_create(request)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)