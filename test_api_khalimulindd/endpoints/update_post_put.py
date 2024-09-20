import requests
from endpoints.endpoint import Endpoint


class UpdatePostPut(Endpoint):
    update_post_id = None

    def update_post(self, created_new_post_id, payload, headers=None):
        self.response = requests.put(
            f'{self.url}/{created_new_post_id}',
            json=payload,
            headers=headers
        )
        print(self.response.json())
        self.json = self.response.json()
        self.update_post_id = self.json['id']
        return self.response
