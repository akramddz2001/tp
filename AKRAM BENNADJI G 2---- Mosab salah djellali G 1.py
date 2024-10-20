import random
import time

def generate_sorted_array(size):
    """Generate a randomly sorted array"""
    array = list(range(size))
    random.shuffle(array)
    array.sort()
    return array

def sequential_search(array, x):
    """Simple sequential search"""
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1

def optimized_sequential_search(array, x):
    """Optimized sequential search"""
    for i in range(len(array)):
        if array[i] > x:
            return -1
        elif array[i] == x:
            return i
    return -1

def binary_search_iterative(array, x):
    """Iterative binary search"""
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(array, x, low, high):
    """Recursive binary search"""
    if low > high:
        return -1
    mid = (low + high) // 2
    if array[mid] == x:
        return mid
    elif array[mid] < x:
        return binary_search_recursive(array, x, mid + 1, high)
    else:
        return binary_search_recursive(array, x, low, mid - 1)

def measure_performance(algorithm, array, x, low=None, high=None):
    """Measure the performance of the algorithm"""
    start = time.time()
    if algorithm == binary_search_recursive:
        result = algorithm(array, x, low, high)
    else:
        result = algorithm(array, x)
    end = time.time()
    return result, end - start

if __name__ == "__main__":
    array_sizes = [10**3, 10**4, 10**5, 10**6]
    algorithms = [sequential_search, optimized_sequential_search, binary_search_iterative, binary_search_recursive]
    
    for size in array_sizes:
        array = generate_sorted_array(size)
        for algorithm in algorithms:
            total_time = 0
            total_comparisons = 0
            for _ in range(100):  # Repeat the experiment 100 times
                x = random.randint(0, size)
                if algorithm == binary_search_recursive:
                    result, time_taken = measure_performance(algorithm, array, x, 0, size - 1)
                else:
                    result, time_taken = measure_performance(algorithm, array, x)
                total_time += time_taken
                # ... (Add code here to count comparisons for each algorithm)
            average_time = total_time / 100
            print(f"Algorithm: {algorithm.__name__}, Size: {size}, Average Time: {average_time:.6f}")
            # ... (Print other results like average comparisons)
