from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import PontosTuristicos
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication


class PontoTuristicoViewSet(ModelViewSet):
    
    #queryset = PontosTuristicos.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ('nome','descricao', '=localizacao__linha1')
    #lookup_field = 'nome'
    
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontosTuristicos.objects.all()
        
        if id:
            queryset = PontosTuristicos.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao) 
            

        return PontosTuristicos.objects.filter(aprovado=True)
    
#   def list (self, request, *args, **Kwargs):
#       return Response({'teste':123})

#    def create(self, request, *args, **kwargs):
#        return Response({'Hello': request.data['nome']})

#   def destroy(self, request, *args, **kwargs):
#       pass
    
#    def retrieve(self, request, *args, **kwargs):
#       pass
    
#    def update(self, request, *args, **kwargs):
#        pass
    
#    def partial_update(self, request, *args, **kwargs):
#        pass
    
    @action(methods=['get'], detail=True)
    def denunciar (self, request, pk=None):
        return Response({"Deu certo"})
        