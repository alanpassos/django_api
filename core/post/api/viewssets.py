from rest_framework import  status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import TokenAuthentication

from post.models import Post
from .serializers import PostSerializer, PostFullSerializer
from core.permissions import IsOwnerPostOrReadOnly


class PostViewsSet(viewsets.ModelViewSet):    
    serializer_class = PostSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields  = ['descricao']
    ordering_fields = ['descricao']
    ordering = ['id']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerPostOrReadOnly]

    def get_queryset(self):
        queryset = Post.objects.all()        
        return queryset

    def list(self, request, *args, **kwargs):
        return super(PostViewsSet,self).list(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def inativos(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(ativo = False)
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PostFullSerializer(page,many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PostFullSerializer(queryset, many=True)     
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def full_posts(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(ativo = True)
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PostFullSerializer(page,many=True)            
            return self.get_paginated_response(serializer.data)

        serializer = PostFullSerializer(queryset, many=True)     
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def full_inativos(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(ativo = False, pessoa__ativo=False)
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PostFullSerializer(page,many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PostFullSerializer(queryset, many=True)     
        return Response(data=serializer.data,status=status.HTTP_200_OK)