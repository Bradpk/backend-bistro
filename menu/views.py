from django.shortcuts import render
from .models import TestTable

from django.http import HttpResponse, JsonResponse
# Think you have to import the models stuff here e.g from models import testtable


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_table(request):
    getit = list(TestTable.object.values())
    return JsonResponse({'data': getit})
