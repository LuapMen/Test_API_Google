import datetime
import os

from requests import Response

class Logier():
    file_name = f"logs/log_{datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')}.log"

    @classmethod
    def write_log_to_file(cls,  date: str):
        with open(cls.file_name, 'a',encoding='utf=8') as logger_file:
            logger_file.write(date)


    @classmethod
    def add_request(cls, url: str , method : str):
        test_name  = os.environ.get("PYTEST_CURRENT_TEST")

        data_to_add = f'\n-----\n'
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request Method: {method}\n"
        data_to_add += f"Request Url: {url}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result: Response):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_add = f" Responce code: {result.status_code}\n"
        data_to_add += f" Responce text {result.text}\n"
        data_to_add += f" Responce headers: {headers_as_dict}\n"
        data_to_add += f" Responce cookies: {cookies_as_dict}\n"
        data_to_add += f'\n-----\n'

        cls.write_log_to_file(data_to_add)