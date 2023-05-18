import sys
import time
import matplotlib.pyplot as plt

def Matrixchain_BF(p, i, j):
    if i == j:
        return 0
    
    _min = sys.maxsize
    
    for k in range(i, j):
        count = (Matrixchain_BF(p, i, k) + Matrixchain_BF(p, k+1, j) + p[i-1] * p[k] * p[j])
        if count < _min:
            _min = count
    
    return _min

arr = [1, 2, 3, 4, 3]
# A1(1x2), A2(2x3), A3(3x4), A4(4x3)
n = len(arr)
print("Minimum number of multiplications is", Matrixchain_BF(arr, 1, n-1))

# Test running time
brute_force_times = []
input_sizes = [5, 10, 15, 20]

for size in input_sizes:
    matrix_sizes = [2] * size  # Generate a list of matrix sizes with the same value
    start_time = time.time()
    Matrixchain_BF(matrix_sizes, 1, size-1)
    end_time = time.time()
    brute_force_times.append(end_time - start_time)

# Plot the running times
plt.plot(input_sizes, brute_force_times, label='Brute Force')
plt.xlabel('Input Size')
plt.ylabel('Running Time (seconds)')
plt.title('Running Times of Matrix Chain Multiplication Algorithm (Brute Force)')
plt.legend()
plt.show()