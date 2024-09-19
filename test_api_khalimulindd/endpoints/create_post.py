import requests
from faker import Faker
from endpoints.endpoint import Endpoint

fake = Faker()


class CreatePost(Endpoint):
    post_id = None

    def create_new_post(self, payload=None, headers=None):
        # Если не передан payload, генерируем случайные данные.
        if payload is None:
            payload = self.generate_random_data_body()

        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.post_id = self.json['id']
        return self.response

    @staticmethod
    def generate_random_names(count=3):
        """Генерация случайных имён"""
        return [fake.company() for _ in range(count)]
