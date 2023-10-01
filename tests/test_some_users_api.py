import pytest
import json
from requests import Response

from utils.api import Users_api
from utils.checking import Checking

"""Create, Update, Delete several users"""


class Test_create_several_user:
    test_data = [("1", "X1"), ("2", "X2"), ("3", "X3"), ("4", "X4")]

    @pytest.mark.parametrize("main_key,value", test_data)
    def test_create_all_users(self, main_key, value):
        print("\n---Method PUT-----\n")

        result_put: Response = Users_api.create_new_user(main_key, value)
        check_put = result_put.json()
        main_key = check_put.get("main_key")
        Checking.check_status_code(result_put, 200)
        # # token = json.loads(result_put.text)
        # # print(list(token))
        Checking.check_json_token(result_put, ['value', 'main_key'])
        Checking.check_json_value(result_put, 'main_key', main_key)
        Checking.check_json_value(result_put, 'value', value)
        print(f"\n Several users were created successfully \n")

    print(" \n------Method GET after creating some users-----------\n")

    def test_get_all_users(self):
        result_get: Response = Users_api.get_new_user()
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(list(token))

        expected_api = [{'main_key': '1', 'value': 'X1'}, {'main_key': '2', 'value': 'X2'},
                        {"main_key": "3", "value": "X3"}, {"main_key": "4", "value": "X4"}]
        Checking.check_json_all_response2(result_get, expected_api)
        print(f"\n Several users data was tested successfully \n")

    print("\n------Method Delete---------\n")

    @pytest.mark.parametrize("main_key,value", test_data)
    def test_delete_all_users(self, main_key, value):
        result_delete: Response = Users_api.delete_user(main_key)
        Checking.check_status_code(result_delete, 200)
        print(f"\n User {main_key} data was deleted successfully \n")

    print("\n-----Method Get after Delete all users-------\n")

    def test_get_after_delete(self):
        result_get: Response = Users_api.get_new_user()
        Checking.check_status_code(result_get, 200)
        Checking.check_json_all_response(result_get, [])
        print("DB is cleaned")

