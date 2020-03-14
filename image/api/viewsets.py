from rest_framework.viewsets import ModelViewSet

from image.api.serializers import AtracaoSerializer
from image.models import Atracao


class AtracoesViewSet(ModelViewSet):
   # permission_classes = (IsAuthenticated,)
   # authentication_classes = (TokenAuthentication,)
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer