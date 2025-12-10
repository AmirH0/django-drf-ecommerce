from rest_framework import serializers

from .models import Category, Product, Brand, ProductLine


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


class ProductLineSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()

    class Meta:
        model = ProductLine
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
