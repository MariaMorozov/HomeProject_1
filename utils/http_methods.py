import requests

"""HTTP methods"""


class Http_methods:
    headers = {'content-Type': 'application/json'}

    @staticmethod
    def get(url):
        result = requests.get(url, headers=Http_methods.headers)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=Http_methods.headers)

        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=Http_methods.headers)

        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=Http_methods.headers)

        return result
