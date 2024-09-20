import requests
import allure
from endpoints.endpoint import Endpoint


class DeletePost(Endpoint):
    message = None

    @allure.step('Delete post')
    def delete_post(self, created_post_id):
        self.response = requests.delete(f"{self.url}/{created_post_id}")
        print(self.response.json())
        print(self.response.status_code)
        if self.response.status_code != 200:
            print(f"Failed to delete post: {self.response.content}")
        self.json = self.response.json()
        self.message = self.json.get('message')
        return self.response

    @allure.step('Check that in massage delete post_id')
    def check_that_post_id_in_massage(self, created_post_id):
        message = self.json.get('message', '')
        assert message == f'Object with id = {created_post_id} has been deleted.'

    @staticmethod
    @allure.step('Check if post is deleted')
    def check_post_deleted(response, post_id):
        if post_id:
            assert response.status_code == 200, 'Expected status code 200 after deletion'
            message = response.json().get('message', '')
            assert str(post_id) in message, f"Post ID {post_id} is not in the deletion message"
        else:
            raise ValueError("Post ID is None")
