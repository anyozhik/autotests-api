from clients.api_client import  APIClient
from httpx import Response

from typing import TypedDict

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    """
    Метод выполняет создание пользователя.

    :param request: Словарь с email, password, lastName, firstName, middleName.
    :return: Ответ от сервера в виде объекта httpx.Response
    """

    def create_user(self, request: CreateUserRequestDict) -> Response:
        return self.client.post("/api/v1/users", json=request)

