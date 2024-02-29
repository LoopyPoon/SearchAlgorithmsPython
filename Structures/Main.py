import random

from Structures.SearchAlgorithms import *
import time

short_list = list(range(10))
long_list = list(range(10_000))
big_long_list = list(range(10_000_000))
duplicated_list = [item for item in long_list for _ in range(2)]  # Добавление каждого элемента дважды
unsorted_list = random.sample(range(1000), 1000)

print("Linear search:")
# Линейный поиск со списком из 10 элементов
print("Short list:")
start_time = time.perf_counter_ns()
res = linear_search(short_list, 7)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

# Линейный поиск со списком из 10_000 элементов
print("Long list:")
start_time = time.perf_counter_ns()
res = linear_search(long_list, 777)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

# Линейный поиск со списком из 10_000_000 элементов
print("Super long list:")
start_time = time.perf_counter_ns()
res = linear_search(big_long_list, 777777)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

# Линейный поиск со списком из 10_000 элементов с повторениями
print("Duplicated list:")
start_time = time.perf_counter_ns()
res = linear_search(duplicated_list, 7)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

# Линейный поиск с неотсортированным списком из 10_000 элементов с повторениями
print("Unsorted duplicated list:")
start_time = time.perf_counter_ns()
res = linear_search(unsorted_list, 7)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

print("\nBinary search:")
# Бинарный поиск со списком из 10 элементов
print("Short list:")
start_time = time.perf_counter_ns()
res = binary_search(short_list, 7)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

# Бинарный поиск со списком из 10_000 элементов
print("Long list:")
start_time = time.perf_counter_ns()
res = binary_search(long_list, 777)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

# Бинарный поиск со списком из 10_000_000 элементов
print("Super long list:")
start_time = time.perf_counter_ns()
res = binary_search(big_long_list, 777777)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

# Бинарный поиск со списком из 10_000 элементов с повторениями
print("Duplicated list:")
start_time = time.perf_counter_ns()
res = binary_search(duplicated_list, 777)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

# Бинарный поиск с неотсортированным списком из 10_000 элементов с повторениями
print("Unsorted duplicated list:")
start_time = time.perf_counter_ns()
res = binary_search(unsorted_list, 777)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

print("\nJump search:")
# Jump search со списком из 10 элементов
print("Short list:")
start_time = time.perf_counter_ns()
res = jump_search(short_list, 7)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

# Jump search со списком из 10_000 элементов
print("Long list:")
start_time = time.perf_counter_ns()
res = jump_search(long_list, 777)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

# Jump search со списком из 10_000_000 элементов
print("Super long list:")
start_time = time.perf_counter_ns()
res = jump_search(big_long_list, 777777)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

# Jump search со списком из 10_000 элементов с повторениями
print("Duplicated list:")
start_time = time.perf_counter_ns()
res = jump_search(duplicated_list, 777)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)

# Jump search с неотсортированным списком из 10_000 элементов с повторениями
print("Unsorted duplicated list:")
start_time = time.perf_counter_ns()
res = jump_search(unsorted_list, 777)
if res == -1:
    print("\tElement not found")
else:
    print("\tElement found at index: ", res)
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("\tTime: ", execution_time)
