from array_ops import ArrayOpsInterface
from static_array import StaticArray
from errors import IndexOverFlowException, SpaceOverFlowException
from typing import Any


class SortedArray(ArrayOpsInterface):

    def __init__(self, max_size: int, type = 'l'):
        self.__max_size = max_size
        self.__arr: StaticArray = StaticArray(max_size, type)
        self.__size: int = 0
    
    def __len__(self) -> int:
        return self.__size

    def __getitem__(self, index: int) -> int:
        self.__checker(index)
        return self.__arr[index]

    def __str__(self) -> str:
        response: str = "< "
        for _ in range(self.__size):
            response += str(self.__arr[_]) + " "
        response += ">"
        return response

    def __checker(self, index: int) -> None:
        if index < 0 or index > self.__size - 1:
            raise IndexOverFlowException(range = (0, self.__size - 1))
    
    def __check_size(self) -> None:
        if self.__size >= self.__max_size:
            raise SpaceOverFlowException(max_space = self.__arr.get_bytes())

    def insert(self, val: Any) -> None:
        self.__check_size()
        if self.__size == 0:
            self.__arr[0] = val
            self.__size += 1
            return
        self.__to_insert: int | None = None
        if val <= self.__arr[0]:
            self.__to_insert = 0 #Insert at the beginning
        elif val >= self.__arr[self.__size - 1]:
            self.__to_insert = self.__size #Insert at the end
        else:
            for i in range(self.__size - 1):
                if self.__arr[i] <= val <= self.__arr[i + 1]:
                    self.__to_insert = i + 1 #Insert somewhere in the middle of the array
        match(self.__to_insert):
            case 0:
                for i in range(self.__size, 0, -1):
                    self.__arr[i] = self.__arr[i - 1]
                self.__arr[0] = val
            case self.__size:
                self.__arr[self.__size] = val
            case _:
                for i in range(self.__size, self.__to_insert, -1):
                    self.__arr[i] = self.__arr[i - 1]
                self.__arr[self.__to_insert] = val
        self.__size += 1
    
    def remove(self, val: Any) -> None:
        self.__id: int | None = self.linear_search(val)
        if self.__id is None:
            return #Cancel the operation because there is nothing to remove
        for _ in range(self.__id, self.__size - 1):
            self.__arr[_] = self.__arr[_ + 1]
        self.__size -= 1

    def linear_search(self, val: Any) -> None | int:
        for ind in range(self.__size):
            if self.__arr[ind] > val:
                return None #The index doesn't exist because val surpass the item value.
            if self.__arr[ind] == val:
                return ind #We got the index

if __name__ == "__main__":
    arr = SortedArray(10)
    arr.insert(1)
    arr.insert(-1)
    arr.insert(-2)
    arr.insert(10)
    arr.insert(2)
    arr.insert(2)
    print(arr)
    arr.remove(2)
    arr.remove(-1)
    print(arr)