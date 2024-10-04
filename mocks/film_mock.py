from dataclasses import dataclass, field
from typing import Union, Optional

from models.film import Film
from repositories.base import Repository


@dataclass
class MockFilmRepository(Repository[Film]):
    films: Optional[dict[int, Film]] = field(default_factory=dict)

    def get(self, id: int) -> Union[Film, None]:
        try:
            return self.films[id]
        except KeyError:
            return None

    def get_all(self, limit: int = 100, offset: int = 0) -> list[Film]:
        return list(self.films.values())

    def add(self, **kwargs: object) -> bool:
        self.films[len(self.films)] = Film(**kwargs)

        return True

    def update(self, id: int, **kwargs: object) -> bool:
        if not id:
            return False

        self.films[id] = Film(**kwargs)

        return True

    def delete(self, id: int) -> bool:
        try:
            del self.films[id]
            return True
        except KeyError:
            return False