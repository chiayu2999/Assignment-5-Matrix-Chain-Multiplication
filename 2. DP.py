#use DP
#m[i,j] = 計算AiAi+1...Aj 所需最少純量乘法次數
#m[i,j] = 0         , if i = j
#       = min(i<=k<j){m[i,k] + m[k+1, j] + Pi-1PkPj}    , if i < j
import sys
import time
import matplotlib.pyplot as plt

def Matrixchain_DP(p):
    n = len(p) - 1

    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = sys.maxsize

            for k in range(i, j):
                tempCost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if tempCost < m[i][j]:
                    m[i][j] = tempCost
                    s[i][j] = k

    return m[1][n], s

def printOptimalParenthesis(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        printOptimalParenthesis(s, i, s[i][j])
        printOptimalParenthesis(s, s[i][j] + 1, j)
        print(")", end="")

arr = [1, 2, 3, 4]
n = len(arr) - 1

minimumMultiplications, solutionMatrix = Matrixchain_DP(arr)

print("Minimum number of scalar multiplications:", minimumMultiplications)
print("Optimal Parenthesization using DP:", end=" ")
printOptimalParenthesis(solutionMatrix, 1, n)

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

# Test running time
DP_times = []
input_sizes = [5, 10, 15, 20]

for size in input_sizes:
    matrix_sizes = [2] * size  # Generate a list of matrix sizes with the same value
    start_time = time.time()
    MatrixChainOrder(matrix_sizes, size)
    end_time = time.time()
    DP_times.append(end_time - start_time)

# Plot the running times
plt.plot(input_sizes, DP_times, label='Dynamic Programming')
plt.xlabel('Input Size')
plt.ylabel('Running Time (seconds)')
plt.title('Running Times of Matrix Chain Multiplication Algorithm (Dynamic Programming)')
plt.legend()
plt.show()

