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

#Удаляем новосозданного пользователя
delete_user_header = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

delete_user_response = httpx.delete(f"http://localhost:8000/api/v1/users/{create_user_data['user']['id']}", headers = delete_user_header)
delete_user_data = delete_user_response.json()
print(f"Статус код удаления : {delete_user_response.status_code}")