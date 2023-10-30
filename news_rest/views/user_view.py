from rest_framework import viewsets
from news_rest.serializers.user_serializer import (
    UserSerializer,
)
from news.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
