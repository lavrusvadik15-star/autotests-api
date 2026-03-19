from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client

class Token(TypedDict):  # Добавили структуру с токенами аутентификации
    """
    Описание структуры аутентификационных токенов.
    то, что мы получим от логина в LoginResponseDict
    """
    tokenType: str
    accessToken: str
    refreshToken: str
class LoginResponseDict(TypedDict):  # Добавили структуру ответа аутентификации
    """
    Описание структуры ответа аутентификации.
    Но в ответе логина приходит формат
    "token": {
        "tokenType": "bearer",
        "accessToken": "string",
        "refreshToken": "string"}
    который надо опять расшифровать
    """
    token: Token


class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str  # Название ключа совпадает с API

class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication2
    """
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)

    #Лайфхак - если нам не нужен полный респонс от логина - создадим еще одну функцию
    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request) # тут мы отправляем запрос на логин
        return response.json() #И из ответа логина берем JSON (т.к. из него нам нужны будут параметры тип токенов и т.д.)

# Добавляем builder для AuthenticationClient с публичным клиентом
def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    #В AuthenticationClient как базовый передали клиент из билдера публичного клиента, т.к. его запросы не требуют авторизации
    #НЕ ЗАБЫВАТЬ ЕГО ИМПОРТИРОВАТЬ ВНАЧАЛЕ (хотя и подтянется само)
    return AuthenticationClient(client=get_public_http_client())