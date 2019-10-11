from rest_framework import  status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication


from pessoa.models import Pessoa
from .serializers import PessoaSerializer,PessoaFullSerializer
from core.permissions import CustomModelPermission,IsOwnerPessoaOrReadOnly

class PessoaViewsSet(viewsets.ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = Pessoa.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    filterset_fields = ['nome']
    search_fields  = ['nome']
    ordering_fields = ['nome']
    ordering = ['id']
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerPessoaOrReadOnly]

    
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
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def full_pessoas(self, request):
        queryset = self.get_queryset().filter(ativo=True)
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PessoaFullSerializer(page,many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PessoaFullSerializer(queryset,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
