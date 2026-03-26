from .get_time import get_time
from arrays.sorted_array import SortedArray
from random import randint
from typing import Any, Tuple

@get_time
def benchmark_ls(arr: SortedArray, target: Any) -> None:
    arr.linear_search(target)

@get_time
def benchmark_bs(arr: SortedArray, target: Any) -> None:
    arr.binary_search(target)

def create_sorted_array(size: int = 3000) -> Tuple[SortedArray, Any]:
    arr: SortedArray = SortedArray(size)
    for _ in range(size):
        arr.insert(randint(-1000, 1000))
    target = arr[randint(0, size - 1)]
    return arr, target

def compare_ls_bs(times: int = 15) -> None:
    ls, bs = [], []
    for _ in range(times):
        arr, target = create_sorted_array()
        ls.append(benchmark_ls(arr, target))
        bs.append(benchmark_bs(arr, target))
        print(f"Results for the {_ + 1}-th array:")
        print(f"Linear Search time >> {ls[_]:.8f}sec")
        print(f"Binary Search time >> {bs[_]:.8f}sec")
    print("-"*20)
    print("Final result:")
    avg_ls = sum(ls)/len(ls)
    avg_bs = sum(bs)/len(bs)
    print(f"Average time for Linear Search: {avg_ls}")
    print(f"Average time for Binary Search: {avg_bs}")
    print(f"Binary search was {avg_ls/avg_bs:.2f} times faster than Linear Search")