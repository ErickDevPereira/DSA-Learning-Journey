from typing import Tuple

class IndexOverFlowException(Exception):
    
    def __init__(self, range: Tuple[int, int]):
        self.__msg = f'Index out of bounds. The indexes must be between {range[0]} and {range[1]}'
        super().__init__(self.__msg)