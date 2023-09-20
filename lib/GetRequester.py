from urllib import response
from flask import Response
import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        pass
    # Send GET request to URL and get response.
        response = requests.get(self.url)

    # Check if request was succesfull
    if response.status_code == 200:
        return response.text # return response body content as a str    
    else:
        raise Exception(f"failed with status code {response.status_code}")
        

    def load_json(self):
        pass
    # Get response body as a string using the get_response_body method
        response_body = self.get_response_body()

    # Load JSON from response body into Python object
        json_data = json.loads(response_body)

        # Return the Python data
        return json_data 