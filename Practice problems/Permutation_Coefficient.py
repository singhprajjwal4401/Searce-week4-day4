#The Permutation Coefficient represented by P(n, k) is used to represent the number of ways to 
#obtain an ordered subset having k elements from a set of n elements.
#time complexity is O(n*k) and space complexity is O(n*k)
def permutationCoeff(n, k):
 
    P = [[0 for i in range(k + 1)]
            for j in range(n + 1)]
 
    # Calculate value of Permutation
    # Coefficient in
    # bottom up manner
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
 
            # Base cases
            if (j == 0):
                P[i][j] = 1
 
            # Calculate value using
            # previously stored values
            else:
                P[i][j] = P[i - 1][j] + (
                        j * P[i - 1][j - 1])
 
            # This step is important
            # as P(i, j) = 0 for j>i
            if (j < k):
                P[i][j + 1] = 0
    return P[n][k]
 
# Driver Code
n = int(input())
k = int(input())
print("Value fo P(", n, ", ", k, ") is ",
    permutationCoeff(n, k), sep = "")
