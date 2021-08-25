from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
# Чтобы вызвать представление, нам нужно назначить его на какой-то URL через конфигурацию URL-ов