import httpx
#Задаем, что будем отправлять в пост
login_payload = {
  "email": "lavrus@example.com",
  "password": "12345"
}
#то запрос через библиотеку с данными
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json = login_payload)
#Новая переменная с джсоном ответа
login_response_data = login_response.json()

print(f"Login response: {login_response_data}")
print(f"Status code: {login_response.status_code}")

#Задаем, что будем отправлять в пост
refresh_payload = {
  "refreshToken": login_response_data['token']['refreshToken']
}
#Запрос
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json = refresh_payload)
#Новая переменная с джсоном ответа
refresh_response_data = refresh_response.json()

print(f"Refresh response: {refresh_response_data}")
print(f"Status code: {refresh_response.status_code}")

#Создаем новые данные, беря их ответа логина токен
me_header = {
        "Authorization" : f"Bearer {login_response_data['token']['accessToken']}"
}

print(me_header)

#Отправляем его в заголовке
user_me = httpx.get("http://localhost:8000/api/v1/users/me", headers = me_header)
me_data = user_me.json()

print(f"Статус запроса me : {user_me.status_code}")
print(f"Это json ответа запроса me : {me_data}")