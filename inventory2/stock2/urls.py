
from django.urls import path
from .views import add_stock_item, stock_item_list

urlpatterns = [
    path('create/', add_stock_item, name='stock_create'),
    path('list/', stock_item_list, name='stock_items'), 
]

