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

def MatrixChainOrder(p, n):
    dp = [[-1 for i in range(n)] for j in range(n)]
    
    def matrixChain_DP(i, j):
        if i == j:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        dp[i][j] = sys.maxsize
        
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], matrixChain_DP(i, k) + matrixChain_DP(k + 1, j) + p[i - 1] * p[k] * p[j])
        
        return dp[i][j]
    
    return matrixChain_DP(1, n - 1)

#test example
arr = [1, 2, 3, 4, 3]
n = len(arr)
print("Minimum number of multiplications (Brute Force):", Matrixchain_BF(arr, 1, n-1))
print("Minimum number of multiplications (Dynamic Programming):", MatrixChainOrder(arr, n))

# Test running time
brute_force_times = []
DP_times = []
input_sizes = [5, 10, 15, 20]

for size in input_sizes:
    matrix_sizes = [2] * size 
    
    # Brute Force
    start_time = time.time()
    Matrixchain_BF(matrix_sizes, 1, size - 1)
    end_time = time.time()
    brute_force_times.append(end_time - start_time)
    
    # Dynamic Programming
    start_time = time.time()
    MatrixChainOrder(matrix_sizes, size)
    end_time = time.time()
    DP_times.append(end_time - start_time)

# Plot the running times
plt.plot(input_sizes, brute_force_times, label='Brute Force')
plt.plot(input_sizes, DP_times, label='Dynamic Programming')
plt.xlabel('Input Size')
plt.ylabel('Running Time (seconds)')
plt.title('Running Times of Matrix Chain Multiplication Algorithms')
plt.legend()
plt.show()
