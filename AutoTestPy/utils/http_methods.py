import requests
from utils.log import Logier
"""List HTTP METHODS"""
class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookies = ""

    @staticmethod
    def get(url):
            Logier.add_request(url, method="GET")
            result = requests.get(url, headers=Http_methods.headers,cookies=Http_methods.cookies)
            Logier.add_response(result)
            return result


    @staticmethod
    def post(url,body):
        Logier.add_request(url, method="post")
        result = requests.post(url,json=body, headers=Http_methods.headers,cookies=Http_methods.cookies)
        Logier.add_response(result)
        return result

    @staticmethod
    def put(url, body):
        Logier.add_request(url, method="PUT")
        result = requests.put(url, json=body, headers=Http_methods.headers , cookies=Http_methods.cookies)
        Logier.add_response(result)
        return result

    @staticmethod
    def delete(url, body):
        Logier.add_request(url, method="DELETE")
        result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logier.add_response(result)
        return result