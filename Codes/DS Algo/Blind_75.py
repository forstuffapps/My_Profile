from functools import *


#-- Array

"""
1. Two Sum (LC number - 1)
"""

def twoSum(nums, target):
    d={}
    n=len(nums)
    for i in range(n):
        b=target-nums[i]

        if b in d:
            return [d[b], i]
        
        d[nums[i]]=i




"""
2. Best Time to Buy and Sell Stock (LC number - 121)
"""

def maxProfit(prices):
    A=list(prices)
    n=len(A)
    B=[0]*n
    m=0
    for i in range(n-1,-1,-1):
        m=max(m,A[i])
        B[i]=m
    

    m=0

    for i in range(n-1):
        m=max(m,B[i]-A[i])


    return m




"""
3. Contains Duplicate (LC number - 217)
"""

def containsDuplicate(nums):
    s=set()

    for i in nums:
        if i in s:
            return True
        s.add(i)
    
    return False



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
4. Longest Common Subsequence  (LC number - 1143)
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
    dp=[[0]*(m+1) for i in range(n+1)]
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



#  Tabulation : Bottom Up
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    n,m=len(text1), len(text2)
    A,B = text1, text2
    dp=[[0]*(m+1) for i in range(n+1)]
    @lru_cache(maxsize=None)
    def z(A,B, n, m):

        for i in range(1,n+1):
            for j in range(1,m+1):

                if A[i-1]==B[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        
        return dp[n][m]
    return z(A,B,n,m)




"""
5. Word Break Problem  (LC number - 139)
"""

def wordBreak( s, wordDict):
    n=len(s)
    dp=[0]*n

    for i in range(n):
        for j in range(i-1,-1,-1):
            if dp[j]!=0 and s[j+1:i+1] in wordDict:
                dp[i]+=1
        else:
            if s[:i+1] in wordDict:
                dp[i]+=1
    
    return dp[-1]!=0



# Another solution handling the special case
def wordBreak(s, wordDict):
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            for j in range(1,i+1):
                if dp[j-1]!=0 and s[j-1:i] in wordDict:
                    dp[i]+=1
                    
        return dp[-1]!=0







"""
6. Combination Sum IV  (LC number - 377)
"""


def combinationSum4(nums, target):
    n=len(nums)
    dp = [0]*(target+1)
    dp[0] = 1
    for i in range(1,target+1):
        for j in range(n):
            if (i-nums[j])>=0:
                dp[i]+=dp[i-nums[j]]
            
    return dp[-1]





"""
7. House Robber  (LC number - 198)
"""

def rob(nums):
        if len(nums)==1:
            return nums[-1]
        n=len(nums)
        m = max(nums[:2])
        c2=nums[0]
        c1 = m
        for i in range(2,n):
            m=max(c1,c2+nums[i])
            c2,c1 = c1,m
        
        return m





"""
8. House Robber 2  (LC number - 213)
they are in circle
"""
def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        n=len(nums)
        def z(nums):
            if len(nums)<3:
                return max(nums)
            
            c2,c1 = nums[0], max(nums[:2])
            n=len(nums)
            for i in range(2,n):
                m=max(c1, c2+nums[i])
                c2,c1 = c1,m
            
            return m
        
        return max(z(nums[0:n-1]), z(nums[1:]))



"""
9. Decode Ways  (LC number - 91)
they are in circle
"""


def numDecodings(s):
        
    n=len(s)
    c2 = 1
    c1 = 1
    if s[0]=='0':
        c1=0
    m=c1
    for i in range(2,n+1):
        m=0
        if 1<=int(s[i-1:i])<=9:
            m+=c1
        if 10<=int(s[i-2:i])<=26:
            m+=c2
        
        c2,c1 = c1,m

    return m


"""
10. Unique Paths  (LC number - 62)
they are in circle
"""


def uniquePaths(m,n):
    dp=[[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i==0 or j==0:
                dp[i][j]=1
    

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    


    return dp[-1][-1]


"""
11. Jump Game  (LC number - 55)
they are in circle
"""


def canJump(nums):
        
    n=len(nums)
    
    m=0

    for i in range(n):
        if i>m:
            return False
        m=max(m,i+nums[i])
    return True


