from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import StockItem

#include this line just icase of decide to optionally ignore  the specified block: @admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    list_display = ('item_code','description','unit_cost','quantity_in_stock','reorder_level')
 

admin.site.register(StockItem, StockItemAdmin) 