import httpx

login_payload = {
  "email": "lavrus@example.com",
  "password": "12345"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json = login_payload)
login_response_data = login_response.json()

print(f"Login response: {login_response_data}")
print(f"Status code: {login_response.status_code}")


# refresh_payload = {
#   "refreshToken": login_response_data['token']['refreshToken']
# }
#
#
# refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json = refresh_payload)
# refresh_response_data = refresh_response.json()
#
# print(f"Refresh response: {refresh_response_data}")
# print(f"Status code: {refresh_response.status_code}")

me_header = {
        "Authorization" : f"Bearer {login_response_data['token']['accessToken']}"
}

print(me_header)


user_me = httpx.get("http://localhost:8000/api/v1/users/me", headers = me_header)
me_data = user_me.json()

print(f"Статус запроса me : {user_me.status_code}")
print(f"Это json ответа запроса me : {me_data}")