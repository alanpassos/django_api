from django.contrib.auth.models import User
from rest_framework import serializers
from pessoa.models import Pessoa

FIELD_ALL = ['id','nome','ativo','user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']    

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = FIELD_ALL

class PessoaFullSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Pessoa
        fields = FIELD_ALL

