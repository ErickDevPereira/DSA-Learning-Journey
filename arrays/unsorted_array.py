from array_ops import ArrayOpsInterface
from static_array import StaticArray
from typing import Any
from errors import SpaceOverFlowException, IndexOverFlowException

class UnsortedArray(ArrayOpsInterface):

    def __init__(self, max_size: int, type: str = 'l'):
        self.__max_size: int = max_size
        self.__arr: StaticArray = StaticArray(self.__max_size, type)
        self.__size: int = 0 #Starting value for the size
    
    def __len__(self) -> int:
        return self.__size
    
    def __getitem__(self, index: int) -> Any:
        self.__checker(index)
        return self.__arr[index]
    
    def __setitem__(self, index: int, value: Any) -> None:
        self.__checker(index)
        self.__arr[index] = value
    
    def __str__(self) -> str:
        response: str = "< "
        for i in range(self.__size):
            response += str(self.__arr[i]) + " "
        response += ">"
        return response

    def __check_size(self) -> None:
        if self.__size >= self.__max_size:
            raise SpaceOverFlowException(max_space = self.__arr.get_bytes())
    
    def __checker(self, index: int) -> None:
        if index < 0 or index >= self.__size:
            raise IndexOverFlowException(range = (0, self.__size - 1))

    def insert(self, val: Any) -> None:
        self.__check_size()
        self.__arr[self.__size] = val
        self.__size += 1
    
    def linear_search(self, val: Any) -> int | None:
        for i in range(self.__size):
            if self.__arr[i] == val:
                return i #Found
        return None #Not found
    
    def remove(self, val: Any) -> None:
        index: int | None = self.linear_search(val)
        if index is not None: #None means that such index wasn't found
            #Swapping the last element by this one without really taking it out, but it will be considered as out of the array because we decrease the size of it.
            self.__arr[index] = self.__arr[self.__size - 1]
            self.__size -= 1 #Reducing the size

if __name__ == "__main__":
    arr = UnsortedArray(2)
    arr.insert(2)
    arr.insert(3)
    arr.insert(4)
    arr.insert(-1)
    arr.insert(0)
    arr.insert(0)
    arr.insert(-1)
    print(arr)
    print(arr.linear_search(-1))