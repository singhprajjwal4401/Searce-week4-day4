# Python Program to find Nth Fibonacci Number using Memoization
def fib(n, memo): 
    # Base case 
    if n == 0 or n == 1 : 
        memo[n] = n 
  
    # If memo[n] is not evaluated before then calculate it 
    if memo[n] is None: 
        memo[n] = fib(n-1 , memo)  + fib(n-2 , memo)  
  
    # return the value corresponding value of n 
    return memo[n] 
  
# Driver program  
def main(): 
    n = 10 
    # Declaration of memo  
    memo = [None]*(101) 
    
    # Calculate and display result
    print("Fibonacci Number is " + str(fib(n, lookup)))
  
if __name__=="__main__": 
    main() 
    
#.............................................................................................................................#    
#2nd method 
# Python Program to find Nth Fibonacci Number using Tabulation
def fib(n): 
  
    # dp array declaration 
    dp = [0]*(n+1) 
  
    # base case 
    dp[1] = 1
  
    # calculating and storing the values 
    for i in xrange(2 , n+1): 
        dp[i] = dp[i-1] + dp[i-2] 
    return dp[n] 
  
# Driver program 
def main(): 
    n = 10
    print("Fibonacci number : " + str(fib(n)))
  
if __name__=="__main__": 
    main() 
