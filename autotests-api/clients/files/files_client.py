from typing import TypedDict

from clients.api_client import APIClient
from httpx import Response


class CreateFileRequestDict(TypedDict) :
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    #любая
    directory: str
    #путь к файлу на локальной машине, который будет загружен
    upload_file : str


class FilesClient(APIClient)  :
    """
    Клиент для работы с /api/v1/files
    """
    def get_file_api (self, file_id) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api (self, request : CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/files",
            data = request,
            #реквест возьмет из своего класса путь и подставим его сюда из реквеста
            files = {"upload_file" : open(request['upload_file'], 'rb')},
        )
    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")
