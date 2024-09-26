import allure
from faker import Faker

fake = Faker()


class Endpoint:
    url = 'https://fakestoreapi.com/products'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that title is the same as sent')
    def check_response_title_is_correct(self, name):
        assert self.json['title'] == name

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200
