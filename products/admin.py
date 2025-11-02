from django.contrib import admin
from .models import Product
from .models import products_for_sale


admin.site.register(Product)
admin.site.register(products_for_sale)
