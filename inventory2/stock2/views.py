from django.shortcuts import render, redirect
from .forms import StockItemForm
from .models import StockItem

def add_stock_item(request):
    if request.method == 'POST':
        form = StockItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list_list')
    else:
        form = StockItemForm()
    return render(request, 'stock2/add_stock_item.html', {'form': form})

def stock_list_view(request):
    stocks = StockItem.objects.all()
    return render(request, 'stock2/stock_item_list.html', {'stock2': stocks})

