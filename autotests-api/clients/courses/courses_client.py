from clients.api_client import APIClient
from typing import TypedDict

from httpx import Response

# Query-параметры (или параметры запроса) – это часть URL, которая передается после знака ? и содержит пары ключ=значение. Несколько параметров передаются через &.
# Пример:
# http://some.url?key1=value1&key2=value2
# В httpx для работы с query-параметрами используется аргумент params. Он принимает словарь, который автоматически преобразуется в query-строку.
# Пример:
# params = {"userId": "12345"}
# Этот словарь будет преобразован в строку запроса:
#?userId=12345

class GetCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов,
    которые мы передадим в query параметр функции, а оттуда подставим в запрос
    """
    userId: str

class CreateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None
class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """
    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        #То есть тут мы в функции получили значения из словаря строкой, и передали их как параметры в GET запрос
        #А GET в APIClient уже умеет работать с query (там прописан такой вариант как params: QueryParams | None = None)
        return self.get("/api/v1/courses", params=query)
    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения ОДНОГО курса по айдишнику.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")