import pytest
from endpoints.create_post import CreatePost
from endpoints.update_post_put import UpdatePostPut
from endpoints.delete_post import DeletePost
from endpoints.update_post_patch import UpdatePostPatch


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
