import httpx

from tools.fakers import get_random_email

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

# Что такое FormData?
# В большинстве API данные отправляются в формате JSON. Однако для загрузки файлов используется формат multipart/form-data.
#
# Это специальный формат, который позволяет отправлять не только текстовые данные, но и файлы.
# Он работает так:
#
# Формируется набор полей (filename, directory и сам файл).
# Данные разбиваются на части (multipart) и упаковываются в FormData.
# Файл передается в потоке байтов, а API сервер обрабатывает его как отдельный вложенный объект.

# Выполняем загрузку файла
create_file_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
create_file_response = httpx.post("http://localhost:8000/api/v1/files",
                                  #т.к. в свагере Form Data мы и передаем дату, а не json
                                  #Название директории любое, оно создастся на сервере в хранилище
                                  data = {"filename" : "image.png", "directory" : "courses"},
                                  #Можно передат и через имя "image.png" просто, а не по пути
                                  #Ключ upload_file соответствует названию параметра в Swagger
                                  files = {"upload_file" : open('./testdata/files/image.png', 'rb')},
                                  headers = create_file_headers)
create_file_response_data = create_file_response.json()
print('Create file data', '(Т.е. наш загруженный файл) :', create_file_response_data)