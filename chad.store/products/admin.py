from django.contrib import admin

# Register your models here.
from .models import Product, ProductTag, Review
admin.site.register(Product)
admin.site.register(ProductTag)
admin.site.register(Review)