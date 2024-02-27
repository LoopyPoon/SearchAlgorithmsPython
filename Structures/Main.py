import random

from Structures.SearchAlgorithms import *
import time

short_list = list(range(10))
long_list = list(range(10_000))
big_long_list = list(range(10_000_000))
duplicated_list = [item for item in long_list for _ in range(2)]  # Добавление каждого элемента дважды
unsorted_list = random.sample(range(1000), 1000)

# Линейный поиск со списком из 10 элементов
start_time = time.perf_counter_ns()
res = linear_search(short_list, 7)
if res == -1:
    print("Element not found")
else:
    print("Element found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Linear search time on a short list: ", execution_time)

# Линейный поиск со списком из 10_000 элементов
start_time = time.perf_counter_ns()
res = linear_search(long_list, 777)
if res == -1:
    print("Element not found")
else:
    print("Element found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Linear search time on a long list: ", execution_time)

# Линейный поиск со списком из 10_000_000 элементов
start_time = time.perf_counter_ns()
res = linear_search(big_long_list, 777777)
if res == -1:
    print("Element not found")
else:
    print("Element found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Linear search time on a super long list: ", execution_time)

# Линейный поиск со списком из 10_000 элементов с повторениями
start_time = time.perf_counter_ns()
res = linear_search(duplicated_list, 7)
if res == -1:
    print("Element not found")
else:
    print("Element found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Linear search time on a duplicated list: ", execution_time)

# Линейный поиск с неотсортированным списком из 10_000 элементов с повторениями
start_time = time.perf_counter_ns()
res = linear_search(unsorted_list, 7)
if res == -1:
    print("Element not found")
else:
    print("Element found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Linear search time on a unsorted duplicated list: ", execution_time)

# Бинарный поиск со списком из 10 элементов
start_time = time.perf_counter_ns()
res = binary_search(short_list, 7)
if res == -1:
    print("Element not found")
else:
    print("Element found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Binary search time on a short list: ", execution_time)

# Бинарный поиск со списком из 10_000 элементов
start_time = time.perf_counter_ns()
res = binary_search(long_list, 777)
if res == -1:
    print("Element not found")
else:
    print("Element found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Binary search time on a long list: ", execution_time)

# Бинарный поиск со списком из 10_000_000 элементов
start_time = time.perf_counter_ns()
res = binary_search(big_long_list, 777777)
if res == -1:
    print("Element not found")
else:
    print("Element found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Binary search time on a super long list: ", execution_time)

# Бинарный поиск со списком из 10_000 элементов с повторениями
start_time = time.perf_counter_ns()
res = binary_search(duplicated_list, 777)
if res == -1:
    print("Element not found")
else:
    print("Element found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Binary search time on a duplicated list: ", execution_time)

# Бинарный поиск с неотсортированным списком из 10_000 элементов с повторениями
start_time = time.perf_counter_ns()
res = binary_search(unsorted_list, 777)
if res == -1:
    print("Element not found")
else:
    print("Element found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Binary search time on a unsorted duplicated list: ", execution_time)
