from rest_framework import serializers
from post.models import Post
from pessoa.api.serializers import PessoaFullSerializer

FIELD_FULL = ['id','descricao','ativo','pessoa']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = FIELD_FULL


class PostFullSerializer(serializers.ModelSerializer):
    pessoa = PessoaFullSerializer()
    class Meta:
        model = Post
        fields = FIELD_FULL
