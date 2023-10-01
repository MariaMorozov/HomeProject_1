import pytest
import json
from requests import Response

from utils.api import Users_api
from utils.checking import Checking

"""Create, Update, Delete single user"""


class Test_create_user:
    test_data = [("Doron1", "1")]

    @pytest.mark.parametrize("main_key,value", test_data)
    def test_create_new_user(self, main_key, value):
        print("\n---Method PUT-----\n")

        result_put: Response = Users_api.create_new_user(main_key, value)       # create new user
        check_put = result_put.json()
        main_key = check_put.get("main_key")
        Checking.check_status_code(result_put, 200)
        # token = json.loads(result_put.text)
        # print(list(token))
        Checking.check_json_token(result_put, ['value', 'main_key'])    # check fields
        Checking.check_json_value(result_put, 'main_key', main_key)     # check main_key field value
        Checking.check_json_value(result_put, 'value', value)           # check value field value
        print(f"\nSingle user {main_key} created with PUT method.\n")

        print(" \n------Method GET after creating-----------\n")
        result_get: Response = Users_api.get_new_user()
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(list(token))

        Checking.check_json_all_response(result_get, [{"value": "1", "main_key": "Doron1"}])
        print(f"\nUser {main_key} tested with GET method\n")

        print("\n-----UPDATE USER with Method POST---\n")
        result_post: Response = Users_api.update_user(main_key)
        Checking.check_status_code(result_post, 200)
        Checking.check_json_value(result_post, 'main_key', main_key)
        Checking.check_json_value(result_post, 'value', "Update test new value")
        print(f"\nUser {main_key} updated with POST method\n")

        print(" \n------Method GET after update-----------\n")
        result_get: Response = Users_api.get_new_user()
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_all_response(result_get, [{"value": "Update test new value", "main_key": "Doron1"}])
        print(f"\nUser {main_key} tested after update with GET method\n")

        print("\n------Method Delete---------\n")
        result_delete: Response = Users_api.delete_user(main_key)
        Checking.check_status_code(result_delete, 200)
        token = json.loads(result_delete.text)
        print(list(token))

        Checking.check_json_value(result_delete, 'main_key', main_key)
        print(f"\nUser {main_key} deleted with DELETE method\n")

        print("\n-----Method Get Delete-------\n")
        result_get: Response = Users_api.get_new_user()
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_all_response(result_get, [])

        print("Create, Update, Delete single user Testing passed successfully")
