from django.contrib import admin
from django.urls import reverse
from .models import Brand, Product, Category, ProductLine, ProductImage
from django.utils.safestring import mark_safe


class EditLinkInline:
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk],
        )

        if instance.pk:
            link = mark_safe("<a href={u}>edit</a>".format(u=url))
            return link
        else:
            return ""


class ProductImageLine(admin.TabularInline):
    model = ProductImage


class ProductLineInLine(EditLinkInline, admin.TabularInline):
    model = ProductLine
    readonly_fields = ("edit",)


# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInLine]


class ProductLineAdmin(admin.ModelAdmin):
    inlines = [ProductImageLine]


# # Register your models here.
admin.site.register(ProductLine, ProductLineAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
