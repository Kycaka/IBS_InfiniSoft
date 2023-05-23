import pytest
import requests
from http import HTTPStatus

from utils.users_data import (
    name_job_list,
    partial_name_job_list,
    login_data_list,
    register_data_list
)
from enums.enums import APIRoutes, GlobalErrors


@pytest.mark.api_test
class TestApi:
    @pytest.mark.parametrize(
            "page",
            [pytest.param(0, marks=pytest.mark.xfail), 1, 2, 3]
        )
    def test_get_list_of_users(self, page):
        response = requests.get(
            url=f'{APIRoutes.LIST_OF_USERS}?page={str(page)}'
        )
        response_body = response.json()
        assert response.status_code == HTTPStatus.OK, \
            GlobalErrors.WRONG_STATUS_CODE
        assert page == response_body["page"], GlobalErrors.WRONG_PAGE_NUMBER

    @pytest.mark.parametrize(
            "user_id",
            [2, pytest.param(23, marks=pytest.mark.xfail)]
        )
    def test_get_single_user(self, user_id):
        response = requests.get(url=f'{APIRoutes.SINGLE_USER}{user_id}')
        response_body = response.json()
        assert response.status_code == HTTPStatus.OK, \
            GlobalErrors.WRONG_STATUS_CODE
        assert response_body["data"] is not None, GlobalErrors.WRONG_USER_DATA

    @pytest.mark.parametrize(
            "resource_id",
            [2, pytest.param(23, marks=pytest.mark.xfail)]
        )
    def test_get_single_resource(self, resource_id):
        response = requests.get(
            url=f'{APIRoutes.SINGLE_RESOURCE}{resource_id}'
        )
        response_body = response.json()
        assert response.status_code == HTTPStatus.OK, \
            GlobalErrors.WRONG_STATUS_CODE

        assert response_body["data"] is not None, \
            GlobalErrors.WRONG_RESOURCE_DATA

    @pytest.mark.parametrize("user_json", name_job_list)
    def test_create_user(self, user_json):
        response = requests.post(
            url=f'{APIRoutes.CREATE_USER}',
            json=user_json
        )
        response_body = response.json()
        assert response.status_code == HTTPStatus.CREATED, \
            GlobalErrors.WRONG_STATUS_CODE

        assert response_body["name"] == user_json["name"]
        assert response_body["job"] == user_json["job"], \
            GlobalErrors.WRONG_DATA_FIELD

    @pytest.mark.parametrize("user_json", name_job_list)
    @pytest.mark.parametrize("user_id", [7, 12])
    def test_put_user(self, user_json, user_id: int):
        response = requests.put(
            url=f'{APIRoutes.EDIT_USER}{user_id}',
            json=user_json
        )
        response_body = response.json()
        assert response.status_code == HTTPStatus.OK, \
            GlobalErrors.WRONG_STATUS_CODE
        assert response_body["name"] == user_json["name"]
        assert response_body["job"] == user_json["job"], \
            GlobalErrors.WRONG_DATA_FIELD

    @pytest.mark.parametrize("part_of_user_json", partial_name_job_list)
    @pytest.mark.parametrize("user_id", [2, 5])
    def test_patch_user(self, user_id, part_of_user_json):
        response = requests.patch(
            url=f'{APIRoutes.EDIT_USER}{user_id}', json=part_of_user_json
        )
        response_body = response.json()
        assert response.status_code == HTTPStatus.OK, \
            GlobalErrors.WRONG_STATUS_CODE
        if 'name' in part_of_user_json:
            assert response_body["name"] == part_of_user_json["name"], \
                GlobalErrors.WRONG_DATA_FIELD
        else:
            assert response_body["job"] == part_of_user_json["job"], \
                GlobalErrors.WRONG_DATA_FIELD

    @pytest.mark.parametrize("user_delete_id", [10, 20])
    def test_delete_user(self, user_delete_id):
        response = requests.delete(
            url=f'{APIRoutes.EDIT_USER}{user_delete_id}'
        )
        assert response.status_code == HTTPStatus.NO_CONTENT, \
            GlobalErrors.WRONG_STATUS_CODE

    @pytest.mark.parametrize("creds_json", register_data_list)
    def test_register_user(self, creds_json):
        response = requests.post(url=f'{APIRoutes.REGISTER}', json=creds_json)
        response_body = response.json()
        assert response.status_code == HTTPStatus.OK, \
            GlobalErrors.WRONG_STATUS_CODE
        assert response_body["token"] is not None, \
            GlobalErrors.WRONG_DATA_FIELD

    @pytest.mark.parametrize("creds_json", login_data_list)
    def test_login_user(self, creds_json):
        response = requests.post(url=f'{APIRoutes.LOGIN}', json=creds_json)
        response_body = response.json()
        assert response.status_code == HTTPStatus.OK, \
            GlobalErrors.WRONG_STATUS_CODE
        assert response_body["token"] is not None, \
            GlobalErrors.WRONG_DATA_FIELD

    @pytest.mark.parametrize("delay", [0, 3])
    def test_get_with_delay(self, delay):
        response = requests.get(url=f'{APIRoutes.DELAYED}{str(delay)}')
        assert response.status_code == HTTPStatus.OK, \
            GlobalErrors.WRONG_STATUS_CODE
