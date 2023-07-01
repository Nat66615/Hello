from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_table_of_multiply(request):
    a = ''
    for i in range(1, 10):
        for j in range(1, 10):
            a += (f'{i} * {j} = {i * j}<br>')
    return HttpResponse(a)
