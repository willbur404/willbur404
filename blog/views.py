from django.shortcuts import render

# Create your views here.


def index(request):
    return render(
        request,
        "blog/index.html",
        context={"title": "My blog", "welcome": "Welcome to my blog"},
    )
