from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class GetExercisesQueryDict(TypedDict):
    """
    Структура запроса (Словарь) для списка упражнений, которые мы передадим в query параметры
    """
    courseId: str
class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса (словаря) на создание упражнения
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса (словаря) на изменение упражнения
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercices
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises/", params=query)

    def create_exercise_api(self, request: CreateExerciseRequestDict ) -> Response:
        """
        Метод создания упражнения
        :param request: Словарь с параметрами
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises/", json=request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения ОДНОГО упражнения по айдишнику.

        :param exercise_id - айдишник упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(self, request: UpdateExerciseRequestDict, exercise_id: str) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения строкой.
        :param request: Словарь с данными курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения по айдишнику.

        :param exercise_id - айдишник упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
