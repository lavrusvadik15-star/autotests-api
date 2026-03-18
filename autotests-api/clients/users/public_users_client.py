from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient



class PublicUsersCreateRequestDict(TypedDict) :
    """
    Описание структуры запроса на публичное создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    def create_user_api(self, request:PublicUsersCreateRequestDict ) -> Response :
        """
        Метод создания пользователя (публичный)
        :param request: Словарь с параметрами создания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("api/v1/users", json = request)
