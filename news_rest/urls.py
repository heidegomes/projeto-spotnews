from django.urls import path
from news_rest.views.category_view import CategoryViewSet
from news_rest.views.user_view import UserViewSet
from news_rest.views.news_view import NewsViewSet


urlpatterns = [
    path("categories", CategoryViewSet, name="categories"),
    path("users", UserViewSet, name="users"),
    path("news", NewsViewSet, name="news"),
]
