from rest_framework import authentication
from payment.models import Services
from .serializers import ServicesSerializer
from rest_framework import viewsets


class ServicesViewSet(viewsets.ModelViewSet):
    serializer_class = ServicesSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Services.objects.all()
