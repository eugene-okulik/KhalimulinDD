import allure
import random
from faker import Faker

fake = Faker()


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that name is the same as sent')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @staticmethod
    def generate_random_data_body():
        """Генерация случайных данных для обьекта"""
        return {
            "name": fake.company(),  # Случайное имя для обновленного поста
            "data": {
                "year": random.randint(2000, 2030),
                "price": round(random.uniform(500.0, 5000.0), 2),
                "CPU model": random.choice(["Intel Core i9", "AMD Ryzen 9", "Intel Core i7", "Apple M1"]),
                "Hard disk size": random.choice(["1 TB", "500 GB", "2 TB"])
            }
        }

    @staticmethod
    def generate_random_base_data_body():
        """Генерация случайных данных для обьекта (без имени)"""
        return {
            "data": {
                "year": random.randint(2000, 2030),
                "price": round(random.uniform(500.0, 5000.0), 2),
                "CPU model": random.choice(["Intel Core i9", "AMD Ryzen 9", "Intel Core i7", "Apple M1"]),
                "Hard disk size": random.choice(["1 TB", "500 GB", "2 TB"])
            }
        }
