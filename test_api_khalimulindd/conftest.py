import pytest
from endpoints.create_post import CreatePost
from endpoints.update_post_put import UpdatePostPut
from endpoints.update_post_patch import UpdatePostPatch
from endpoints.delete_post import DeletePost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_put_endpoint():
    return UpdatePostPut()


@pytest.fixture()
def update_post_patch_endpoint():
    return UpdatePostPatch()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


@pytest.fixture()
def create_post(create_post_endpoint):
    """Фикстура для создания поста с произвольным payload"""
    def _create_post(payload=None):
        create_post_endpoint.create_new_post(payload=payload)
        return create_post_endpoint
    return _create_post


@pytest.fixture()
def create_and_cleanup_post(create_post_endpoint, delete_post_endpoint):
    """Создает пост и удаляет его после завершения теста."""
    create_post_endpoint.create_new_post()
    yield create_post_endpoint

    # После завершения теста удаляем пост
    created_post_id = create_post_endpoint.post_id
    if created_post_id:
        delete_response = delete_post_endpoint.delete_post(created_post_id)
        create_post_endpoint.delete_response = delete_response


@pytest.fixture()
def create_post_fixture(create_post_endpoint):
    """Фикстура для создания поста"""
    create_post_endpoint.create_new_post()
    return create_post_endpoint


@pytest.fixture()
def cleanup_post_fixture(delete_post_endpoint):
    """Фикстура для удаления"""
    def _cleanup_post(post_id):
        if post_id:
            delete_post_endpoint.delete_post(post_id)
    return _cleanup_post
