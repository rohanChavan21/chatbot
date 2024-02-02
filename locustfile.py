import json
import requests
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between requests in seconds

    @task
    def call_endpoint(self):
        query = "Algorithms"
        num = 7  # Assuming num is a predefined variable
        url = "http://localhost:5000/similarity_search"
        payload = {'query': query, 'k': num}
        headers = {'Content-Type': 'application/json'}

        response = self.client.post(url, data=json.dumps(payload), headers=headers)

        print(response.status_code)