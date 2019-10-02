from rest_framework import serializers
from post.models import Post
from pessoa.api.serializers import PessoaSerializer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','descricao','ativo']


class PostFullSerializer(serializers.ModelSerializer):
    pessoa = PessoaSerializer()
    class Meta:
        model = Post
        fields = ['id','descricao','ativo', 'pessoa']
