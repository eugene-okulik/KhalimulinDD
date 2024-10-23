from locust import task, HttpUser
from faker import Faker
import random

fake = Faker()


class Product(HttpUser):
    headers = None

    # Создание продукта
    @task(1)
    def post_product(self):
        data_body_product = {
            "title": fake.company(),
            "price": round(random.uniform(500.0, 5000.0), 2),
            "description": 'lorem ipsum set',
            "image": 'https://i.pravatar.cc',
            "category": 'electronic'
        }

        self.headers = {'Content-type': 'application/json'}

        self.client.post('/products', headers=self.headers, json=data_body_product)

    # Получение всех продуктов
    @task(1)
    def get_all_products(self):
        self.client.get('/products', headers=self.headers)

    # Получение одного продуктов
    @task(3)
    def get_one_product(self):
        for product_id in range(1, 10):
            self.client.get(f"/products/{product_id}", headers=self.headers)
