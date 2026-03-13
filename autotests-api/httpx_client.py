import httpx
from tools.fakers import get_random_email

#Создаем пользователя
create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_data = create_user_response.json()
print(f"create_user_data : {create_user_data}")

#Авторизовываемся
login_payload = {
    "email":create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json = login_payload)
login_response_data = login_response.json()
print(f"login_data : {login_response_data}")

#Создаем переменную клиент - через нее будут идти все запрос. Передаем в нее необходимые параметры (общая часть адреса, таймауты, авторизацию)
client = httpx.Client(base_url="http://localhost:8000",
                      timeout=100,
                      headers= {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"})

get_user_me_response = client.get("/api/v1/users/me")
get_user_me_response_data = get_user_me_response.json()

print(f"get_user_me_response_data {get_user_me_response_data}")
print(f"Это текст такой же, без джсона если надо {get_user_me_response.text}")