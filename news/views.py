from django.shortcuts import render
from news.models import News


def index(request):
    context = {"title": "Spot News", "news": News.objects.all()}
    return render(request, "home.html", context)
