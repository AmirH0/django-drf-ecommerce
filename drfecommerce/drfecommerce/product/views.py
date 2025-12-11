from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db import connection
from django.db.models import Prefetch


class CategoryView(viewsets.ViewSet):

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        # print(self.queryset)

        return Response(serializer.data)


class BrandView(viewsets.ViewSet):

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductView(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    # queryset = Product.objects.all().select_related("category", "brand")
    queryset = (
        Product.objects.isactive()
        .select_related("category", "brand")
        .prefetch_related(Prefetch("product_line"))
        .prefetch_related(Prefetch("product_line__product_image"))
    )
    
    # queryset = Product.isactive.all().select_related("category", "brand")

    serializer_class = ProductSerializer
    lookup_field = "slug"

    # فیلترها فعال می‌شن
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    # فیلترهای DjangoFilter
    filterset_fields = {
        "category__name": ["exact", "icontains"],
        # "brand__name": ["exact"],
        # "price": ["gte", "lte"],
        "is_active": ["exact"],
    }

    # سرچ → icontains
    search_fields = ["name", "description"]

    # سورت‌کردن
    ordering_fields = ["name"]
    # ordering = ["-created_at"]  # پیش‌فرض


# class ProductView(viewsets.ViewSet):
#     # serializer_class = ProductSerializer
#     queryset = Product.objects.all()

#     # print(queryset)
#     @extend_schema(
#         parameters=[
#             OpenApiParameter(
#                 name="category",
#                 description="Filter products by category name",
#                 required=False,
#                 type=str,
#                 location=OpenApiParameter.QUERY,
#             ),
#         ]
#     )
#     def list(self, request, *args, **kwargs):
#         queryset = self.queryset
#         category = request.query_params.get("category")

#         if category:
#             queryset = queryset.filter(category__name=category)

#         serializer = ProductSerializer(queryset, many=True)
#         x = Response(serializer.data)
#         print(connection.queries)
#         return


# @action(methods=["get"], detail=False, url_path=r"category/(?p<category>\w+)/all")
# def list_product_by_category(self, request, category=None):
#     serializer = ProductSerializer(
#         self.queryset.filter(category__name=category), many=True
#     )
#     return Response(serializer.data)
