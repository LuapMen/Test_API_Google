from utils.http_methods import Http_methods

"""List API METHOD FROM GOODLE MAPS """

base_URL = "https://rahulshettyacademy.com"  #Base URL
key = "?key=qaclick123" #Parameter for all requests


class Google_maps_api():

    @staticmethod
    def create_new_place():


        post_resourse = "/maps/api/place/add/json" #Post resoure form merhod Post
        post_url = base_URL + post_resourse + key
        print(post_url)
        json_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }

        resaut_post = Http_methods.post( post_url, json_create_new_place)
        print(resaut_post.text)
        return resaut_post