from django.shortcuts import render, redirect, get_object_or_404
from news.models import News, Category
from news.forms import CreateNewModelForm, CreateCategorieModelForm


def index(request):
    context = {"title": "Spot News", "news": News.objects.all()}
    return render(request, "home.html", context)


def new_details(request, id):
    new = get_object_or_404(News, id=id)
    context = {"new": new}
    return render(request, "news_details.html", context)


def create_categories(request):
    form = CreateCategorieModelForm()
    if request.method == "POST":
        form = CreateCategorieModelForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")
    context = {"form": form}
    return render(request, "categories_form.html", context)


def create_news(request):
    form = CreateNewModelForm()
    if request.method == "POST":
        form = CreateNewModelForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.cleaned_data.pop("categories")
            News.objects.create(**form.cleaned_data)
            News.objects.set(category)
            return redirect("home-page")
    context = {"form": form}
    return render(request, "news_form.html", context)
