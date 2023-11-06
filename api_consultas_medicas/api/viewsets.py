from rest_framework import viewsets, generics
from api_consultas_medicas.api import serializers
from api_consultas_medicas import models

class PessoaProfissionalViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PessoaProfissionalSerializer
    queryset = models.PessoaProfissional.objects.all()

class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ConsultaSerializer
    queryset = models.Consulta.objects.all()

class ConsultasPorProfissionais(generics.ListAPIView):
    def get_queryset(self):
        queryset = models.Consulta.objects.filter(pessoa_profissional_id=self.kwargs['pk'])       
        return queryset
    serializer_class = serializers.ConsultasPorProfissionaisSerializer