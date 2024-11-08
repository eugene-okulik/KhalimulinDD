import pytest
from endpoints.create_product import CreateProduct
from endpoints.update_product_put import UpdateProductPut
from endpoints.update_product_patch import UpdateProductPatch
from endpoints.delete_product import DeleteProduct


@pytest.fixture()
def create_product_endpoint():
    return CreateProduct()


@pytest.fixture()
def update_product_put_endpoint():
    return UpdateProductPut()


@pytest.fixture()
def update_product_patch_endpoint():
    return UpdateProductPatch()


@pytest.fixture()
def delete_product_endpoint():
    return DeleteProduct()


@pytest.fixture()
def create_and_product_fixture(create_product_endpoint, delete_product_endpoint):
    """Фикстура для создания и удаления продукта"""
    create_product_endpoint.create_new_product()
    created_product_id = create_product_endpoint.product_id
    yield created_product_id
    delete_product_endpoint.delete_product(created_product_id)


@pytest.fixture()
def create_product_fixture(create_product_endpoint):
    """Фикстура для создания продукта"""
    created_product_id = create_product_endpoint.create_new_product()
    yield created_product_id


@pytest.fixture()
def cleanup_product_fixture(request):
    """Фикстура для удаления продукта после выполнения теста."""
    yield
    product_id = request.function.product_id
    delete_product = DeleteProduct()
    delete_product.delete_product(created_product_id=product_id)
