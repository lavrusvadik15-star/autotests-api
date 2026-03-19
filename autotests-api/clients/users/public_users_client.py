from typing import TypedDict

from httpx import Response
from clients.public_http_builder import get_public_http_client
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
    """
    Клиент для работы с публичным API пользователей.

    Предоставляет методы для взаимодействия с эндпоинтами пользователей,
    доступными без аутентификации (например, регистрация)
    """
    def create_user_api(self, request:PublicUsersCreateRequestDict ) -> Response :
        """
        Метод создания пользователя (публичный)
        :param request: Словарь с параметрами создания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json = request)

# Добавляем builder для PublicUsersClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())