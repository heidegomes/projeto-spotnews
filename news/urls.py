from django.urls import path
from news.views import index, new_details, create_news, create_categories


urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:id>", new_details, name="news-details-page"),
    path("categories", create_categories, name="categories-form"),
    path("news", create_news, name="news-form"),
]
