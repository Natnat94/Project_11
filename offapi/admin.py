from django.contrib import admin
from .models import Product, Category, Store, ProductSaved
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Store)
admin.site.register(ProductSaved)
