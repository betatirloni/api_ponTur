from rest_framework.serializers import ModelSerializer
from localizacao.models import Localizacao

class LocalizacaoSerializer(ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ('linha1', 'linha2', 'cidade', 'estado', 'pais', 'longitude', 'latitude')