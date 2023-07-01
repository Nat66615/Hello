from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_beautiful_table(request):
    return render(request, 'beauty/table.html')
