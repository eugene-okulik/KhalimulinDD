import requests
import allure
from endpoints.endpoint import Endpoint


class DeletePost(Endpoint):
    message = None

    @allure.step('Delete post')
    def delete_post(self, created_post_id):
        self.response = requests.delete(f"{self.url}/{created_post_id}")
        self.json = self.response.json()
        self.message = self.json.get('message')
        return self.response

    @allure.step('Check that in massage delete post_id')
    def check_that_post_id_in_massage(self, created_post_id):
        message = self.json.get('message', '')
        expected_message = f'Object with id = {created_post_id} has been deleted.'
        assert message == expected_message, f"Expected message '{expected_message}', but got '{message}'"
