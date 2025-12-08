from rest_framework import serializers

from .models import Category, Product, Brand


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.CharField(read_only=True, source="parent.name")

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "parent",
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"
