from utils.Api import Google_maps_api


class Test_create_place():

    def test_create_new_place(selfs):

        print("Method Post")
        result_post: Responce = Google_maps_api.create_new_place()


