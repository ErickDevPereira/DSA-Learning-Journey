from abc import ABC, abstractmethod

class ArrayOpsInterface(ABC):

    @abstractmethod
    def linear_search(self) -> int | None: pass

    @abstractmethod
    def insert(self) -> None: pass

    @abstractmethod
    def remove(self) -> None: pass