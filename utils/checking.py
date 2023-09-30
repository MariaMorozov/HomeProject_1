import json
from requests import Response

"""Methods for test results"""


class Checking():
    """Method for status_code testing"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("OK. Identical Status code = " + str(response.status_code))

        else:
            print("Failure. NOT Identical Status code = " + str(response.status_code))

    """Test method for mandatory fields existing"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All fields exist")

    """Test method for fields values"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " value is ok")

    """Test method for fields values"""

    @staticmethod
    def check_json_all_response(response: Response, expected_value):
        check = response.json()
        assert check == expected_value
        print("GET response same as expected. -ok")

    @staticmethod
    def check_json_all_response2(response: Response, expected_value):
        check = response.json()
        sorted_list = sorted(check, key=lambda d: d['main_key'])
        assert sorted_list == expected_value
        print("2GET response same as expected. -ok")
        print(sorted_list)

    """Test method for fields values per expected word in value"""

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(field_name + " contains expected word. Test is ok. the word is " + search_word)
        else:
            print(field_name + " doesn't contain expected word. Test failed. the word is " + search_word)



