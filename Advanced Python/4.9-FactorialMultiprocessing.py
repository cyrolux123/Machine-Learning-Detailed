'''
Real-World Example :: Multiprocessing for CPU-bound tasks
Scenario : Factorial Calculation
Factorial calculations, especially for large numbers, inolve significant computational work. Multiprocessing can be used to distribute the workload across multiple CPU cores, improving performance.
'''

import multiprocessing
import math
import sys
import time

# function to calculate factorial
def factorial(number):
    print(f"Calculating factorial of {number}...")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010, 10011, 10012, 10013, 10014, 10015]

    start_time = time.time()

    # Create a pool of  worker processes  
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)

    end_time = time.time()
    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")