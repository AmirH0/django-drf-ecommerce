import pytest
from django.core.checks import Error
from drfecommerce.product.fields import OrderField
from drfecommerce.product.models import Brand ,Product , ProductLine ,Category
# pytestmark = pytest.mark.django_db
from django.db import models

@pytest.mark.django_db
class TestCategoryModel:
    def test_str_method(self, category_factory):
        category = category_factory()
        assert str(category) == "test_category"


class TestBrandmodel:
    pass


class TestProductModel:
    pass

@pytest.mark.django_db
def test_orderfield_assigns_incremental_values():
    # Create required foreign keys
    brand = Brand.objects.create(name="Brand A")
    category = Category.objects.create(name="Cat A")
    
    # Create product (NOT NULL brand required)
    product = Product.objects.create(
        name="Test Product",
        descripition="test", 
        is_digital=False,
        slug="test-product",
        brand=brand,
        category=category,
        is_active=True,
    )

    # Create product lines (NOT NULL: price, sku, stock_qty, product)
    pl1 = ProductLine.objects.create(
        product=product,
        price=10,
        sku="SKU1",
        stock_qty=100,
        is_active=True,
    )
    pl2 = ProductLine.objects.create(
        product=product,
        price=20,
        sku="SKU2",
        stock_qty=100,
        is_active=True,
    )
    pl3 = ProductLine.objects.create(
        product=product,
        price=30,
        sku="SKU3",
        stock_qty=100,
        is_active=True,
    )

    assert pl1.order == 1
    assert pl2.order == 2
    assert pl3.order == 3