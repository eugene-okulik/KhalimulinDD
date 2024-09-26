import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteProduct(Endpoint):

    @allure.step('Delete product')
    def delete_product(self, created_product_id):
        self.response = requests.delete(f"{self.url}/{created_product_id}")
        print(f"\nУдаление продукта с ID: {created_product_id}, Статус ответа: {self.response.status_code}")
        self.json = self.response.json()
        return self.response
