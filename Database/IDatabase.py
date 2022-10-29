from abc import ABC, abstractmethod


class IDatabase(ABC):
    @abstractmethod
    def save_last_city_for_user(self, user_id: int, city: str) -> None:
        pass

    @abstractmethod
    def get_last_city_by_user_id(self, user_id: int) -> str:
        pass
