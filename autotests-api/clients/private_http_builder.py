from typing import TypedDict

from httpx import Client

from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict

# Структура данных пользователя для авторизации.
# Создали заново, а не взяли из LoginRequestDict - потому что билдер должен быть независим от апи клиентов
class AuthenticationUserDict(TypedDict):
    email: str
    password: str

# Создаем private builder
def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # Инициализируем AuthenticationClient для аутентификации
    #просто новая переменная, которая вызовет билдер аутентификации (чтобы он в свою очередь подтянул публичный клиент из публичного билдера)
    #и вернет готовый АПИ клиент аутенфикации
    authentication_client = get_authentication_client()
    # Инициализируем запрос на аутентификацию
    #Т.е. новая переменная, которая передаст ВХОДНЫЕ данные словаря LoginRequestDict (который используется в клиенте аутентификации)
    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    # Выполняем POST запрос и логнимся
    #По запросу login который мы специально добавляли извлекать токены
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        # Добавляем заголовок авторизации, который мы заберем из ответа login(выше). Получается пирамида обратная
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )
