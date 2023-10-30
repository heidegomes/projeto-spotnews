from rest_framework import viewsets
from news_rest.serializers.category_serializer import (
    CategorySerializer,
)
from news.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
