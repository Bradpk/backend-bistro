from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get/', views.get_table, name='get_table'),
    #path('getmenu/', views.get_menu, name='get_menu'),
]