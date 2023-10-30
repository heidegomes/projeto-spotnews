from django.shortcuts import render, redirect, get_object_or_404
from news.models import News
from news.forms import CreateNewModelForm


def index(request):
    context = {"title": "Spot News", "news": News.objects.all()}
    return render(request, "home.html", context)


def new_details(request, id):
    new = get_object_or_404(News, id=id)
    context = {"new": new}
    return render(request, "news_details.html", context)


def create_categories(request):
    form = CreateNewModelForm()
    context = {"form": form}
    return render(request, "categories_form.html", context)


def create_news(request):
    form = CreateNewModelForm()
    if request.method == "POST":
        form = CreateNewModelForm(request.POST)
        if form.is_valid():
            News.objects.create(**form.cleaned_data)
            return redirect("home-page")
    context = {"form": form}
    return render(request, "news_form.html", context)
