from django.contrib import admin
from news.models import Category, User, News

admin.site.register(Category)
admin.site.register(User)
admin.site.register(News)
