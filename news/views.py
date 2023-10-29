from django.shortcuts import render
from news.models import News
from django.shortcuts import get_object_or_404


def index(request):
    context = {"title": "Spot News", "news": News.objects.all()}
    return render(request, "home.html", context)


def new_details(request, id):
    new = get_object_or_404(News, id=id)
    return render(request, "news_details.html", {"new": new})
