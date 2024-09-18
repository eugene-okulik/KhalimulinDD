import requests
from endpoints.endpoint import Endpoint


class CreatePost(Endpoint):
    post_id = None

    def create_new_post(self, payload, headers=None):
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.post_id = self.json['id']
        print(self.response.json())
        return self.response
