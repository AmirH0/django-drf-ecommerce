from rest_framework import serializers

from .models import Category, Product, Brand, ProductLine, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.CharField(read_only=True, source="parent.name")

    class Meta:
        model = Category
        fields = [
            "name",
            "parent",
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class ProductImageserializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ("id",)


class ProductLineSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    product_image = ProductImageserializer(many=True)

    class Meta:
        model = ProductLine
        fields = ["price", "sku", "stock_qty", "order", "product_image"]


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
