import random
import time
import pandas as pd


def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


def generate_data(size, data_type):
    if data_type == "pseudolosowe":
        return [random.randint(1, 1000000) for _ in range(size)]
    elif data_type == "posortowane":
        return sorted([random.randint(1, 1000000) for _ in range(size)])
    elif data_type == "wielokrotne":
        unique_values = [random.randint(1, 1000000) for _ in range(64)]
        return [random.choice(unique_values) for _ in range(size)]


sizes = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768,65536,131072,262144]  # (za długi czas oczekiwania) na kolejne 2^n-te wartości
data_types = ["pseudolosowe", "posortowane", "wielokrotne"]
results = []
for data_type in data_types:
    for size in sizes:
        data = generate_data(size, data_type)
        start_time = time.perf_counter()
        shell_sort(data)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        results.append({"Sortowanie": "Shell", "Dane": data_type, "Rozmiar": size, "Czas (s)": elapsed_time})

print(results)
