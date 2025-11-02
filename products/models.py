from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Chips','Chips'),
        ('Drinks','Drinks'),
        ('Bisquits', 'Bisquits'),
        ('Gums', 'Gums'),

    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class products_for_sale(models.Model):
    sale_name = models.CharField(max_length=100)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_image = models.ImageField(upload_to='sale_products/', blank=True, null=True)
    
    def __str__(self):
        return self.sale_name
