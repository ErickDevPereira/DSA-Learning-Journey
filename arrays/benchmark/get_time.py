from typing import Callable
import time

def get_time(f: Callable) -> float:

    def wrapper(*args, **kwargs):
       start: int = time.time()
       f(*args, **kwargs)
       end: int = time.time()
       return end - start

    return wrapper