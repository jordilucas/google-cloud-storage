from rest_framework.serializers import ModelSerializer

from image.models import Atracao


class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id','foto')