from django.shortcuts import render
from .models import TestTable, MenuItem
# MenuItem, Category, Cuisine
from django.http import HttpResponse, JsonResponse
# Think you have to import the models stuff here e.g from models import testtable
#---------------------------------------------------------------------------------------------------------------------------------
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
#---------------------------------------------------------------------------------------------------------------------------------
def get_table(request):
    getit = list(TestTable.objects.values())
    return JsonResponse({'data': getit})
#---------------------------------------------------------------------------------------------------------------------------------
def get_menu(request):
    menu_items = MenuItem.objects.select_related().all()
    data = []

    for item in menu_items:
        data.append({
            'title': item.title,
            'description': item.description,
            'price': float(item.price),
            'spicy_level': item.spicy_level,
            'category': item.category.name,
            'cuisine': item.cuisine.name,
        })

    return JsonResponse(data, safe=False)
