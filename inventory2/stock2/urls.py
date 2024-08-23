
from django.urls import path
from .views import add_stock_item, stock_list_view

urlpatterns = [
    path('create/', add_stock_item, name='stock_create'),
    path('list', stock_list_view, name='stock_list'), 
]