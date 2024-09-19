import requests
from endpoints.endpoint import Endpoint


class UpdatePostPatch(Endpoint):
    update_post_id = None

    def update_post_patch(self, created_new_post_id, payload, headers=None):
        self.response = requests.patch(
            f'{self.url}/{created_new_post_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.update_post_id = self.json['id']
        return self.response
