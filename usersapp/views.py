from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import mixins, viewsets
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
