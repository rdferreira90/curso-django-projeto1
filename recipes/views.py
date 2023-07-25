from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "recipes/home.html", context={"name": "Rodrigo Ferreira"})


def contato(request):
    return render(request, "apague-me/temp.html")


def sobre(request):
    return HttpResponse("sobre")
