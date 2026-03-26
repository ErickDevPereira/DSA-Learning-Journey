from array import array
from errors import OverFlowException

class StaticArray:

    def __init__(self, size: int, type: str = 'l'):
        #Setting the standard value for the entries of an empty array
        match(type):
            case 'u' | 'w':
                self.__init_val: str = " "
            case 'd' | 'f':
                self.__init_val: float = 0.0
            case _:
                self.__init_val: int = 0
        self.__size: int = size
        #The array from array class is private, so we can't shrink or expand the StaticArray object
        self.__arr: array = array(type, [self.__init_val] * self.__size)

    def __len__(self) -> int:
        return self.__size
    
    def __getitem__(self, index: int) -> None:
        self.__checker(index)#Checking the indexes
        return self.__arr[index]
    
    def __setitem__(self, index: int, val: int | float | str) -> None:
        self.__checker(index)#Checking the indexes
        self.__arr[index] = val
    
    def __str__(self) -> str:
        response: str = "< "
        for i in range(self.__size):
            response += str(self.__arr[i]) + " "
        response += ">"
        return response
    
    def __checker(self, index: int) -> None:
        if index < 0 or index > self.__size - 1:
            raise OverFlowException(range = (0, self.__size))