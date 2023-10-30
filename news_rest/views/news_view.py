from rest_framework import viewsets
from news_rest.serializers.news_serializer import (
    NewsSerializer,
)
from news.models import News


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
