from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from pontos_turisticos.models import PontosTuristicos
from atracoes.api.serializers import AtracaoSerializer
from localizacao.api.serializers import LocalizacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    localizacao = LocalizacaoSerializer()
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    descricao_completa = SerializerMethodField()
    class Meta:
        model = PontosTuristicos
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'localizacao', 'descricao_completa', 'descricao_completa2')
        
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)    