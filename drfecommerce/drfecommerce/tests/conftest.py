from pytest_factoryboy import register

from .factories import CategoryFactory, ProductFactory, BrandFactory, ProductLineFactory

import pytest
from rest_framework.test import APIClient


register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(ProductLineFactory)


@pytest.fixture
def api_client():
    return APIClient()
