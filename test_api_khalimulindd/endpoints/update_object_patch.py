import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateObjectPatch(Endpoint):
    update_object_id = None
    update_object_name = None

    @allure.step('Update object PATCH')
    def update_object_patch(self, created_new_object_id, payload, headers=None):
        self.response = requests.patch(
            f'{self.url}/{created_new_object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.update_object_id = self.json['id']
        self.update_object_name = self.json['name']
        return self.response
