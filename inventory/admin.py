from django.contrib import admin
from .models import Supplier, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supplier', 'description', 'stock', 'availability')
    list_display_links = ('id', 'name')
    list_filter = ('supplier',)
    list_editable = ('stock', 'availability')
    search_fields = ('name', 'description', 'supplier__name')
    list_per_page = 50
admin.site.register(Product, ProductAdmin)

admin.site.register(Supplier)