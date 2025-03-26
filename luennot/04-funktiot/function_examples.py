"""
NOTE!

If you run this as is the output will be a bit messy.
It might be easier to copy and paste these functions and their usage codes to a
separate file. Just make sure to add any necessary imports in your own file.

Each new section starts with a comment of two percent signs.
# %%
"""

from typing import Callable, Any, Dict


# %%
# 1. Financial Calculation: Monthly Loan Payment
def calculate_monthly_payment(principal: float, annual_rate: float, years: int) -> float:
    """
    Calculate monthly loan payment using the amortization formula.
    
    Args:
        principal (float): The loan amount.
        annual_rate (float): Annual interest rate (in percent).
        years (int): Loan term in years.
    
    Returns:
        float: Monthly payment.
    """
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return payment

# Example usage:
loan_amount = 200_000
annual_interest = 5
loan_term = 30
print("Monthly Payment: ", 
      calculate_monthly_payment(loan_amount, 
                                annual_interest, 
                                loan_term), 
      " euro")


# %%
# 2. Logging with Decorators: Tracking Function Calls
def logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to log function call details."""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a: int, b: int) -> int:
    return a + b

# Example usage:
print("Sum:", add(5, 3))


# %%
# 3. File Processing: Counting Error Lines in a Log File
def process_log_file(file_path: str) -> int:
    """
    Process a log file and count how many lines contain the word 'ERROR'.
    
    Args:
        file_path (str): Path to the log file.
    
    Returns:
        int: Number of error lines.
    """
    error_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
    return error_count

# Example usage:
# Assuming a log file 'app.log' exists in the working directory:
# print("Error count:", process_log_file("app.log"))


# %%
# 4. Recursion: Flattening a Nested Dictionary
def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Recursively flattens a nested dictionary.
    
    Args:
        d (Dict[str, Any]): The dictionary to flatten.
        parent_key (str): The base key string.
        sep (str): Separator between keys.
    
    Returns:
        Dict[str, Any]: A flattened dictionary.
    """
    items: Dict[str, Any] = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

# Example usage:
nested = {'user': {'name': 'Alice', 'age': 30}, 'location': 'Wonderland'}
print("Flattened dict:", flatten_dict(nested))


# %%
# 5. Lambda Functions: Sorting a List of Dictionaries by a Key
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort the list by the 'age' key using a lambda function.
sorted_data = sorted(data, key=lambda x: x["age"])
print("Sorted data by age:", sorted_data)


# %%
# 6. Variable-Length Arguments: Logging Sensor Data
def log_sensor_data(timestamp: str, *readings: float, **sensor_info: Any) -> None:
    """
    Log sensor data with a timestamp, multiple readings, and additional sensor details.
    
    Args:
        timestamp (str): The time of the log entry.
        *readings (float): A variable number of sensor readings.
        **sensor_info: Additional keyword information about the sensor.
    """
    print(f"Timestamp: {timestamp}")
    print("Readings:")
    for reading in readings:
        print(f" - {reading}")
    print("Sensor Info:")
    for key, value in sensor_info.items():
        print(f" {key}: {value}")

# Example usage:
log_sensor_data("2025-02-27 12:00", 23.4, 25.1, 22.8, location="Room A", sensor_id="S1")


# %%
# 7. Higher-Order Functions: Creating a Discount Calculator
def discount_calculator(discount_percentage: float) -> Callable[[float], float]:
    """
    Return a function that applies a given discount percentage to a price.
    
    Args:
        discount_percentage (float): The discount percentage to apply.
    
    Returns:
        Callable[[float], float]: A function that takes a price and returns the discounted price.
    """
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount

# Example usage:
apply_20_discount = discount_calculator(20)
print("Discounted price:", apply_20_discount(100))


# %%
# 8. Memoization Decorator: Optimizing Recursive Fibonacci Calculation
def cache_results(func: Callable[[int], int]) -> Callable[[int], int]:
    """Decorator to cache function results for faster repeated calls."""
    cache: Dict[int, int] = {}
    def wrapper(n: int) -> int:
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper

@cache_results
def factorial(n: int) -> int:
    """
    Compute the factorial of n recursively.
    
    Args:
        n (int): The factorial to compute.
    
    Returns:
        int: The result.
    """
    if n < 2:
        return n
    return factorial(n - 1) + factorial(n - 2)

# Example usage:
print("factorial(10):", factorial(10))

# With this you can test how caching affects the execution time
import time

def time_function(func, *args, **kwargs):
    """Time how long a function takes to execute."""
    start_time = time.time()
    result = func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    return result, elapsed_time

def test_factorial_caching(n: int = 35):
    # First call (will compute and cache results)
    result, elapsed_first = time_function(factorial, n)
    print(f"First call: factorial({n}) = {result}, took {elapsed_first:.6f} seconds")
    
    # Second call (should be faster because of caching)
    result, elapsed_second = time_function(factorial, n)
    print(f"Second call: factorial({n}) = {result}, took {elapsed_second:.6f} seconds")

# Run the test
test_factorial_caching()
