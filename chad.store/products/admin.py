from django.contrib import admin

# Register your models here.
from .models import Product, ProductTag, Review, ProductImage,  FavoriteProduct, Cart

class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(ProductTag)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(FavoriteProduct)
admin.site.register(ProductImage)