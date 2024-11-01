## Multithreading
# When to use multithreading
#  I/O-bound tasks : Tasks that spend most of their time waiting for input/output operations to complete.
# Concurrent tasks : When you want to improve the throughput of your application by processing multiple tasks concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")


# Create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()

# start the threads
t1.start()
t2.start()

# wait for the threads to finish
t1.join()
t2.join()

finished_time = time.time() - t
print(finished_time)