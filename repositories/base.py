from abc import ABC, abstractmethod
from typing import Union


class Repository[T](ABC):

    @abstractmethod
    def get(self, id: int) -> Union[T, None]:
        raise NotImplementedError

    @abstractmethod
    def get_all(self, limit: int, offset: int) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def add(self, **kwargs: object) -> bool:
        raise NotImplementedError

    @abstractmethod
    def update(self, **kwargs: object) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> bool:
        raise NotImplementedError