import allure


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
        assert self.response.status_code == 200, f'In response status {self.response.status_code}'
