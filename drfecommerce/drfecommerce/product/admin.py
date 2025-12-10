from django.contrib import admin

from .models import Brand, Product, Category, ProductLine


class ProductLineInLine(admin.TabularInline):
    model = ProductLine


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInLine]


# Register your models here.

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
