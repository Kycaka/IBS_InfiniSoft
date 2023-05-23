from requests import get, post, put, delete, patch

from enums.enums import GlobalErrors


class ApiClient:
    @staticmethod
    def get_reqres(host, path):
        url = host + path
        return get(url)

    @staticmethod
    def post_reqres(host, path, body):
        url = host + path
        return post(url, body)

    @staticmethod
    def put_reqres(host, path, body):
        url = host + path
        return put(url, body)

    @staticmethod
    def patch_reqres(host, path, body):
        url = host + path
        return patch(url, body)

    @staticmethod
    def delete_reqres(host, path):
        url = host + path
        return delete(url)

    @staticmethod
    def is_response_code_correct(response, expected_status_code: int):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, \
            GlobalErrors.WRONG_STATUS_CODE
