from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)
        if ((username is not None) and (password is not None)):
            user = User.objects.create_user(username, None, password)
            user.is_superuser = True
            user.save()
        return user