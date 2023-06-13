from utils.Api import Google_maps_api
from requests import Response
from utils.chekiing import Check_ing

class Test_create_place():

    def test_create_new_place(selfs):

        print("Method Post")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Check_ing.check_status_code (result_post, 200)

        print("Method Get Post")
        result_get = Google_maps_api.get_new_place(place_id)
        Check_ing.check_status_code(result_get, 200)

        print("Method Put")
        result_put = Google_maps_api.put_new_place(place_id)
        Check_ing.check_status_code(result_put, 200)

        print("Method Get Put")
        result_get = Google_maps_api.get_new_place(place_id)
        Check_ing.check_status_code(result_get, 200)

        print("Method delete")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Check_ing.check_status_code(result_delete, 200)

        print("Method Get Delete")
        result_get = Google_maps_api.get_new_place(place_id)
        Check_ing.check_status_code(result_get, 404)