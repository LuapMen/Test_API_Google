"""Method for check status code """
from requests import Response
class Check_ing():

    """Method for check """
    @staticmethod
    def check_status_code(response : Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Success . Code stasus : " + str(response.status_code))
        else:
            print("Fail . Code stasus : " + str(response.status_code))

