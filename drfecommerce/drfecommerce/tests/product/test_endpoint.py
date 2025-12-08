import pytest
from django.urls import reverse

@pytest.mark.django_db
class TestCategoryEndpoint:

    endpoint = "/api/category/"

    def test_category_get(self, api_client, category_factory):
        category_factory()

        response = api_client.get(self.endpoint)

        assert response.status_code == 200


@pytest.mark.django_db
class TestBrandEndpoint:

    endpoint = "/api/brand/"

    def test_brand_get(self, api_client, brand_factory):
        brand_factory()

        response = api_client.get(self.endpoint)

        assert response.status_code == 200


@pytest.mark.django_db
class TestProductEndpoint:

    endpoint = "/api/product/"

    def test_product_get(self, api_client, product_factory):
        product_factory.create_batch(3)
        # url = reverse("product-list")
        response = api_client.get(self.endpoint)

        assert response.status_code == 200

        assert len(response.data) == 3

        assert "name" in response.data[0]
