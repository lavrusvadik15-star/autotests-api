import httpx

# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
# print(response.status_code)
# print(response.json())
#
# data = {
#     "title" : "ТЕСТ",
#     "completed" : False,
#     "userId" : 1
#
# }
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
#
# print(response.status_code)
# print(response.json())
# #print(response.request.headers)
#
# dara = {
#     "username": "name",
#     "password": "12345"
# }
# response = httpx.post("https://httpbin.org/post", data = data)
# print(response.status_code)
# print(response.json())
# #print(response.request.headers)
#
# headers = {
#     "Autor" : "Secret"
# }
# response = httpx.get("https://httpbin.org/get", headers = headers)
# print(response.status_code)
# print(response.json())
#
# response = httpx.get("https://jsonplaceholder.typicode.com/todos?userId=1")
# print(response.url)
# print(response.json())
#
# params = {
#     "userID" : 1
# }
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
# print(response.url)
# print(response.json())
#
# files = {"file" : ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files = files)
# print(response.json())
#
# with httpx.Client() as client :
#     response1= client.get ("https://jsonplaceholder.typicode.com/todos/1")
#     response2= client.get("https://jsonplaceholder.typicode.com/todos/1")
# print(response1.json())
# print(response2.json())
#
# client = httpx.Client(headers = {"Autor" : "Secret"})
# response = client.get("https://httpbin.org/get")
# print(response.json())
try :
    response = httpx.get("https://jsonplaceholder.typicode.com/invalidTEST")
    #print(response.status_code)
    response.raise_for_status()
except httpx.HTTPError as e:
    print(f"ОШИБКА апроса {e}")

try :
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout :
    print(f"Проблема с таймаутом c теста")