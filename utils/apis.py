import requests

class APIS:
    BASE_URL = "https://petstore.swagger.io/v2"

    def __init__(self):
        self.header = {"Content-Type": "application/json"}

    def post(self, endpoint, payload=None):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url=url, headers=self.header, json=payload)
        return response

    def get(self, endpoint, params=None):
        url = f"{self.BASE_URL}/{endpoint}"
        return requests.get(url=url, headers=self.header, params=params)

    def put(self, endpoint, payload=None):
        url = f"{self.BASE_URL}/{endpoint}"
        return requests.put(url=url, headers=self.header, json=payload)

    def delete(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        return requests.delete(url=url, headers=self.header)