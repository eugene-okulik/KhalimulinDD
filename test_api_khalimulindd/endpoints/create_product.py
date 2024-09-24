import requests
import allure
from faker import Faker
from endpoints.endpoint import Endpoint

fake = Faker()


@allure.step('Created product')
class CreateProduct(Endpoint):
    product_id = None

    def create_new_product(self, headers=None):

        payload = self.data_body()

        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        print(f'\nСоздание обьекта {self.response.json()}')
        self.json = self.response.json()
        self.product_id = self.json['id']
        return self.product_id

    @staticmethod
    def generate_random_names(count=3):
        """Генерация случайных названий"""
        return [fake.company() for _ in range(count)]

    @staticmethod
    def data_body():
        """Тело запроса с генерацией случайного названия для продукта"""
        return {
            "title": fake.company(),  # Случайное название для обновленного продукта
            "price": 13.5,
            "description": "lorem ipsum set",
            "image": "https://i.pravatar.cc",
            "category": "electronic"
        }

    @staticmethod
    def data_body_is_not_title():
        """Тело запроса для продукта (без названия)"""
        return {
            "price": 13.5,
            "description": "lorem ipsum set",
            "image": "https://i.pravatar.cc",
            "category": "electronic"
        }
