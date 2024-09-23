import requests
import allure
from faker import Faker
from endpoints.endpoint import Endpoint

fake = Faker()


@allure.step('Created object')
class CreateObject(Endpoint):
    object_id = None
    object_name = None

    def create_new_object(self, payload=None, headers=None):
        # Если не передан payload, генерируем случайные данные.
        if payload is None:
            payload = self.generate_random_data_body()

        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.object_id = self.json['id']
        self.object_name = self.json['name']
        return self.response

    @staticmethod
    def generate_random_names(count=3):
        """Генерация случайных имён"""
        return [fake.company() for _ in range(count)]
