import heapq
import numpy as np
from collections import deque


np.random.seed(seed=12345)


def get_numbers(n: int = 1_000) -> np.array:
    return np.random.randint(-1000, 1001, size=n)


if __name__ == "__main__":

    # ----- (1) heapifying -----
    list_ = list(get_numbers(n=10))
    print(f"Before heapifying: {list_=}")
    heapq.heapify(list_)
    print(f"After heapifying: {list_=}")

    # ----- (2) popping from heap: heapq.heappop -----
    list_ = list(get_numbers(n=15))
    heapq.heapify(list_)
    for i in range(len(list_)):
        print(f"{i+1}: {heapq.heappop(list_)}")

    # ----- (3) pushing onto heap -----
    heap_ = []
    for x in get_numbers(n=10):
        heapq.heappush(heap_, x)
    print(f"{heap_=}")

    # ----- (4) nlargest, nsmallest -----
    list_ = list(get_numbers(n=10))
    print(f"{list_=}")
    print(f"{heapq.nlargest(3, list_)=}")
    print(f"{heapq.nsmallest(3, list_)=}")
