from utils.http_methods import Http_methods

"""List API METHOD FROM GOODLE MAPS """

base_URL = "https://rahulshettyacademy.com"  #Base URL
key = "?key=qaclick123" #Parameter for all requests

class Google_maps_api():
    """Method Post"""
    @staticmethod
    def create_new_place():

        post_resourse = "/maps/api/place/add/json" #Post resoure
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
    """Method get"""
    @staticmethod
    def get_new_place(place_id):

        get_resorurse = "/maps/api/place/get/json" ##GET resoure
        get_url = base_URL + get_resorurse + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        # print(result_get.text)                         #TUPLE
        # return result_get

    """Method PUT / update information """
    @staticmethod
    def put_new_place(place_id):
        put_resorurse = "/maps/api/place/update/json"  #PUT resoure
        put_url = base_URL +put_resorurse + key
        print(put_url)
        json_for_updatate_new_location = {
            "place_id": place_id,
            "address": "Ukraine Forever, UA",
            "key": "qaclick123"

        }
        result_put = Http_methods.put(put_url , json_for_updatate_new_location)
        print(result_put.text)
        return result_put

    """Method Delete / Delete location """
    @staticmethod
    def delete_new_place(place_id):
        delete_resorurse = "/maps/api/place/delete/json"  #PUT delete
        delete_url = base_URL + delete_resorurse + key
        print(delete_url)
        json_for_delete_location = {
            "place_id": place_id,
        }
        result_delete = Http_methods.delete(delete_url , json_for_delete_location)
        print(result_delete.text)
        return result_delete

