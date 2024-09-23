import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    message = None

    @allure.step('Delete object')
    def delete_object(self, created_object_id):
        self.response = requests.delete(f"{self.url}/{created_object_id}")
        self.json = self.response.json()
        self.message = self.json.get('message')
        return self.response

    @allure.step('Check that in massage delete object_id')
    def check_that_object_id_in_massage(self, created_object_id):
        message = self.json.get('message', '')
        assert created_object_id in message
