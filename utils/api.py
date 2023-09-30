from utils.http_methods import Http_methods

"""Methods for users api testing"""
base_url = "https://l761dniu80.execute-api.us-east-2.amazonaws.com/default/exercise_api"  # base URL


class Users_api:
    """Create new users method - PUT"""

    @staticmethod
    def create_new_user(main_key, value):
        json_for_create_new_user = {
            "value": value,
            "main_key": main_key
        }
        result_put = Http_methods.put(base_url, json_for_create_new_user)
        print(result_put.text)
        return result_put

    """Test new location method - Get"""

    @staticmethod
    def get_new_user():

        result_get = Http_methods.get(base_url)
        print(result_get.text)
        return result_get

    """Update new location method - Post"""

    @staticmethod
    def update_user(main_key):

        json_for_update_user = {
            "main_key": main_key,
            "value": "Update test new value"
        }
        result_post = Http_methods.post(base_url, json_for_update_user)
        print(result_post.text)
        return result_post

    # """Delete new location method - Put"""

    @staticmethod
    def delete_user(main_key):
        json_for_delete_user = {
            "main_key": main_key
        }
        result_delete = Http_methods.delete(base_url, json_for_delete_user)
        print(result_delete.text)
        return result_delete
