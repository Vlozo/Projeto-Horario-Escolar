from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World!")
