import time
from typing import Callable, Dict, Tuple



#%%
def cache_results(func: Callable[[int], int]) -> Callable[[int], int]:
    cache: Dict[int, int] = {}

    def wrapper(n: int) -> int:
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper


#%%
@cache_results
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


#%%


def time_function(func: Callable, *args: Tuple, **kwargs: Dict):
    start_time = time.time()
    result = func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    return (result, elapsed_time)


def test_factorial_caching(n: int = 35):
    result, elapsed_time = time_function(factorial, n)
    print(f"First call: factorial({n}), took {elapsed_time:.6f} seconds")

    result, elapsed_time = time_function(factorial, n)
    print(f"Second call: factorial({n}), took {elapsed_time:.6f} seconds")


#%%
# test_factorial_caching(1000)
for i in range(12):
    test_factorial_caching(i * 100)
#%%
test_factorial_caching(1100)
