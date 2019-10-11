from django.contrib.auth.models import User
from rest_framework import serializers
from pessoa.models import Pessoa
from user.api.serializers import UserSerializer

FIELD_ALL = ['id','nome','ativo','user']

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = FIELD_ALL

class PessoaFullSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Pessoa
        fields = FIELD_ALL

