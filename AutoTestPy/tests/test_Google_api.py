from utils.Api import Google_maps_api


class Test_create_place():

    def test_create_new_place(selfs):

        print("Method Post")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("Method Get")
        result_get = Google_maps_api.get_new_place(place_id)

