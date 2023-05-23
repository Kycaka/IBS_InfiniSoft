from enum import Enum


class APIRoutes(str, Enum):
    BASE_URL = 'https://reqres.in/'

    LIST_OF_USERS = f'{BASE_URL}api/users'
    SINGLE_USER = f'{BASE_URL}api/users/'
    LIST_OF_RESOURCE = f'{BASE_URL}api/unknown'
    SINGLE_RESOURCE = f'{BASE_URL}api/unknown/'
    CREATE_USER = f'{BASE_URL}api/users'
    EDIT_USER = f'{BASE_URL}api/users/'
    REGISTER = f'{BASE_URL}api/register'
    LOGIN = f'{BASE_URL}api/login'
    DELAYED = f'{BASE_URL}api/users?delay='

    def __str__(self) -> str:
        return self.value


class GlobalErrors(Enum):
    WRONG_STATUS_CODE = 'Статус код отличен от ожидаемого'
    WRONG_DATA_FIELD = 'Одно или несколько полей не совпадают с ожидаемыми'
    WRONG_PAGE_NUMBER = 'Полученная страница отличается от ожидаемой'
    WRONG_USER_DATA = 'Информация о пользователе отсутствует'
    WRONG_RESOURCE_DATA = 'Информация о ресурсе отсутствует'
