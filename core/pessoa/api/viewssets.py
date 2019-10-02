from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

from pessoa.models import Pessoa
from .serializers import PessoaSerializer

class PessoaViewsSet(viewsets.ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = Pessoa.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields  = ['nome']
    ordering_fields = ['nome']
    ordering = ['id']

    
    def list(self, request, *args, **kwargs):
        return super(PessoaViewsSet,self).list(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def inativos(self, request):
        queryset = self.get_queryset().filter(ativo=False)
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PessoaSerializer(page,many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PessoaSerializer(queryset,many=True)
        return Response(data=serializer.data)
