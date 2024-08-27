import random
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from constants import OPTIONS


data_1 = [123134, 431134, 13134, 4525, 53331, 3765, 3455, 4361, 5424, 35, 3633, 5, 4253, 3352]
data_2 = [12321114, 15214531, 16451423, 17421513, 1032443, 2252134, 5442541, 432452, 345243, 532245, 3242533, 1422340]


def generate_random_sequence(length):
    nucleotides = ('A', 'C', 'G', 'T')
    sequence = ''.join(random.choice(nucleotides) for _ in range(length))
    return sequence


def run_generation(length_list, mode):
    if mode == 'sync':
        results = []
        for length in length_list:
            results.append(generate_random_sequence(length))
        return results

    if mode == 'threads':
        with ThreadPoolExecutor() as executor:
            results = executor.map(generate_random_sequence, length_list)
            return results

    if mode == 'processes':
        with ProcessPoolExecutor() as executor:
            results = executor.map(generate_random_sequence, length_list)
            return results


if __name__ == "__main__":
    timer = []

    # change the data (data_1, data_2)
    data = data_1

    start = time.time()
    run_generation(data, OPTIONS.SYNCHRONOUS.value)
    end = time.time()
    timer.append(end - start)
    print(f"Sync: {timer[0]:.2f} seconds")

    start = time.time()
    run_generation(data, OPTIONS.THREADS.value)
    end = time.time()
    timer.append(end - start)
    print(f"Threads: {timer[1]:.2f} seconds")

    start = time.time()
    run_generation(data, OPTIONS.PROCESSES.value)
    end = time.time()
    timer.append(end - start)
    print(f"Processes: {timer[2]:.2f} seconds")
