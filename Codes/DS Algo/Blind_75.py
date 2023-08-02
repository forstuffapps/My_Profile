from functools import *



#-- DP

"""
1. Climbing Stairs (LC number - 70)
"""

# Tabulation : Bottom-Up Approach
def climbStairs(n):
    dp=[0]*(n+1)
    dp[0],dp[1]=1,1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    
    return dp[n]


# Recursive : Top-Down Approach
def climbStairs(n):
    @lru_cache(maxsize=None)
    def z(n):
        if n==0 or n==1:
            return 1
        return z(n-1) + z(n-2)
    return z(n)




"""
2. Coin Change (LC number - 322)
"""

def coinChange(coins, amount):
    n=amount
    g=10**9+7
    m=len(coins)
    dp = [0]*(n+1)
    dp[0]=0
    for i in range(1,n+1):
        k=g
        for j in range(m):
            if (i-coins[j])>=0 and dp[i-coins[j]]!=g:
                k=min(k,dp[i-coins[j]])
        if k!=g:
            dp[i]=k+1
        else:
            dp[i]=k
    print(dp)
    if dp[n]==g:
        return -1
    return dp[n]



def coinChange(coins, amount):
    @lru_cache(maxsize=None)
    def z(coins,amount):
        A=amount
        if A<0:
            return None
        if A==0:
            return 0
        
        m=10**9+7
        n=len(coins)
        for j in range(n):
            k=z(coins, A-coins[j])
            if k!=None:
                m=min(m,k)
            
        return None if m==10**9+7 else m+1
    
    k=z(tuple(coins), amount)

    return -1 if k==None else k



"""
3. Longest Increasing Subsequence  (LC number - 300)
"""

def lengthOfLIS(nums):
    n=len(nums)

    dp=[0]*(n)
    dp[0]=1

    for i in range(1,n):
        m=0
        for j in range(i-1,-1,-1):
            if nums[j]<nums[i]:
                m=max(m,dp[j])
        
        dp[i]=m+1
    #print(dp)
    return max(dp)




"""
3. Longest Common Subsequence  (LC number - 1143)
"""

#  Recursion 
def longestCommonSubsequence(text1, text2):
    n,m=len(text1), len(text2)
    A,B = text1, text2
    @lru_cache(maxsize=None)
    def z(A,B, n, m):
        if n==0 or m==0:
            return 0
        if A[n-1]==B[m-1]:
            return 1+z(A,B,n-1,m-1)
        else:
            return max(z(A,B,n-1,m), z(A,B,n,m-1))
    
    return z(A,B,n,m)


#  Recursion + Memorization
def longestCommonSubsequence(text1, text2):
    n,m=len(text1), len(text2)
    A,B = text1, text2
    dp=[[0]*(m+1)]*(n+1)
    @lru_cache(maxsize=None)
    def z(A,B, n, m):

        if n==0 or m==0:
            return 0
        if A[n-1]==B[m-1]:
            dp[n][m] = 1+z(A,B,n-1,m-1)
        else:
            dp[n][m] = max(z(A,B,n-1,m), z(A,B,n,m-1))
        
        return dp[n][m]
    return z(A,B,n,m)