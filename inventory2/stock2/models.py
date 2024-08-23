from django.db import models

# Create your models here.
class StockItem(models.Model):
    item_code = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=100)
    unit_cost = models.DecimalField(decimal_places=2, max_digits=5)
    quantity_in_stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField()

    def __str__(self):
        return f"{self.item_code} {self.reorder_level}"