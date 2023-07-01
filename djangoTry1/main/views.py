from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

today = datetime.now


# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'date': today})


def get_page_multiply(request):
    return render(request, 'main/multiply.html')
