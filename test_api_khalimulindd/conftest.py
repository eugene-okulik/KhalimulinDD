import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object_put import UpdateObjectPut
from endpoints.update_object_patch import UpdateObjectPatch
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_put_endpoint():
    return UpdateObjectPut()


@pytest.fixture()
def update_object_patch_endpoint():
    return UpdateObjectPatch()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def create_object_fixture(create_object_endpoint):
    """Фикстура для создания обьекта"""
    def _create_object(payload=None):
        create_object_endpoint.create_new_object(payload=payload)
        created_object_id = create_object_endpoint.object_id
        created_name = create_object_endpoint.object_name
        return create_object_endpoint, created_object_id, created_name
    return _create_object


@pytest.fixture()
def update_put_object_fixture(update_object_put_endpoint):
    """Фикстура для изменения обьекта"""
    def _update_object(payload=None):
        update_object_put_endpoint.update_object_put(payload=payload)
        update_object_id = update_object_put_endpoint.update_object_id
        update_name = update_object_put_endpoint.update_object_name
        return update_object_put_endpoint, update_object_id, update_name
    return _update_object


@pytest.fixture()
def update_patch_object_fixture(update_object_patch_endpoint):
    """Фикстура для частичного изменения обьекта"""
    def _update_object(payload=None):
        update_object_patch_endpoint.update_object_patch(payload=payload)
        update_object_id = update_object_patch_endpoint.update_object_id
        update_name = update_object_patch_endpoint.update_object_name
        return update_object_patch_endpoint, update_object_id, update_name
    return _update_object


@pytest.fixture()
def cleanup_object_fixture(delete_object_endpoint):
    """Фикстура для удаления обьекта"""
    def _cleanup_object(object_id):
        if object_id:
            delete_object_endpoint.delete_object(object_id)
    return _cleanup_object
