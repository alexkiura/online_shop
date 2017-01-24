"""Configurations for admin site."""

from django.contrib import admin
from shop.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    """Admin site confifguration for Category model."""
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    """Admin site configuration for Product model."""
    list_display = ['name', 'slug', 'price', 'stock',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
