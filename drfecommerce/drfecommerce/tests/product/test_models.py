import pytest

# pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestCategoryModel:
    def test_str_method(self , category_factory):
        category = category_factory()
        assert str(category) == "test_category"


class TestBrandmodel:
    pass


class TestProductModel:
    pass
