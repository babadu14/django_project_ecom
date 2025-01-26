from django.contrib import admin
from .models import Category, CategoryImage
# Register your models here.

class ImageInline(admin.StackedInline):
    model = CategoryImage
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(CategoryImage)