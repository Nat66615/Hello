from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_programmers_day(request):
    return HttpResponse('<h3>В обычный год день программиста - 13го сентября, в высокосный - 12го сентября</h3>')
