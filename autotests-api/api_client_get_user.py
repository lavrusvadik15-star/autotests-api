from clients.authentication.authentication_client import get_authentication_client
from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersCreateRequestDict
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя (просто словарь с входными данными для запроса)
create_user_request = PublicUsersCreateRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

# Отправляем POST запрос на создание пользователя
#помним, что create_user_api ждет словарь с данными входными
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_data = create_user_response.json()
print(f'Create_user_data (т.е. данные созданного пользователя) : {create_user_response_data}')

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password'],
)
# Инициализируем клиент PrivateUsersClient (он там ждет только логин-пароль, чтобы создать приватный клиент, что выше и добавили)
private_users_client = get_private_users_client(authentication_user)

# Отправляем GET запрос на получение данных пользователя
get_user_response = private_users_client.get_user_api(create_user_response_data['user']['id'])
get_user_response_data = get_user_response.json()
print(f'Get_user_response_data (Т.е. ответ с проверкой данных пользователя): {get_user_response_data}')