from typing import Union

from database.database_connection import DatabaseConnection
from models.film import Film
from utils import DATABASE_CONFIG_DICT
from .base import Repository

connection = DatabaseConnection(config=DATABASE_CONFIG_DICT)


class FilmRepository(Repository[Film]):

    def get(self, id: int) -> Union[Film, None]:
        with connection.connect() as cursor:
            cursor.execute("SELECT * FROM film WHERE film_id = %s", (id,))

            result = cursor.fetchone()

            if not result:
                return None

            return Film(*result)

    def add(self, **kwargs: object) -> bool:
        ...

    def delete(self, id: int) -> bool:
        try:
            with connection.connect() as cursor:
                cursor.execute("DELETE FROM film WHERE film_id = %s", (id,))

                return cursor.rowcount > 0
        except Exception as err:
            print(f'Error: {err}')
            return False

    def get_all(self, limit: int = 100, offset: int = 0) -> list[Film]:
        with connection.connect() as cursor:
            cursor.execute('SELECT * FROM film ORDER BY film_id LIMIT %s OFFSET %s;', (limit, offset))

            results = cursor.fetchall()

            if not results:
                return []

            film_list = [Film(*result_temp) for result_temp in results]

            return film_list

    def update(self, id: int, **kwargs: object) -> bool:
        ...