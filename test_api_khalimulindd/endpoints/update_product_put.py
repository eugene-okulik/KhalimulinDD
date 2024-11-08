import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateProductPut(Endpoint):
    update_product_id = None
    update_product_title = None

    @allure.step('Update product PUT')
    def update_product_put(self, created_new_product_id, payload, headers=None):
        self.response = requests.put(
            f'{self.url}/{created_new_product_id}',
            json=payload,
            headers=headers
        )
        print(f'\nИзменение обьекта {self.response.json()}')
        self.json = self.response.json()
        self.update_product_id = self.json['id']
        self.update_product_title = self.json['title']
        return self.response
