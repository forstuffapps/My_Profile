#-- 20 Patterns of DP





#-- Pattern - 1
"""
Fibonacci Sequence

LeetCode Problems:
LeetCode 70: Climbing Stairs
LeetCode 509: Fibonacci Number
LeetCode 746. Min Cost Climbing Stairs
"""


"""
LeetCode 70: Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""


def climbStairs(n):
    dp=[0]*(n+1)
    dp[0],dp[1]=1,1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    
    return dp[n]




"""
LeetCode 509: Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number 
is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
"""


def fib(n):
    l=[0,1]
    for i in range(2,31):
        l.append(l[-1]+l[-2])
    

    return l[n]




"""
LeetCode 746. Min Cost Climbing Stairs
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you 
can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
"""



def minCostClimbingStairs(cost):
    n = len(cost)
    p2,p1 = 0,0
    for i in range(2, n+1):
        c = min(p2+cost[i-2], p1+cost[i-1])
        p2, p1 = p1, c
    
    return c


############################################################################################


#-- Pattern - 2

"""
Kadane's Algorithm

LeetCode Problems:
LeetCode 53: Maximum Subarray
LeetCode 918: Maximum Sum Circular Subarray
LeetCode 152: Maximum Product Subarray
"""




"""
LeetCode 53: Maximum Subarray
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""



def maxSubArray(nums):
    n=len(nums)
    g = 10**9+7
    z,c = -g,0
    for i in range(n):
        c = max(c+nums[i], nums[i])
        z = max(z,c)
    
    return z





"""
LeetCode 918: Maximum Sum Circular Subarray
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
A circular array means the end of the array connects to the beginning of the array. Formally, the next element of 
nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], 
nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Solution : https://leetcode.com/problems/maximum-sum-circular-subarray/solutions/178422/one-pass
"""


def maxSubarraySumCircular(nums):
    g = 10**9+7
    c_min, z_min = g, g
    c_max, z_max = -g, -g
    t=0
    for i in nums:
        t+=i
        c_min = min(c_min+i, i)
        c_max = max(c_max+i, i)
        z_min = min(z_min, c_min)
        z_max = max(z_max, c_max)
    
    if t==z_min:
        return z_max
    return max(z_max, t-z_min)





"""
LeetCode 152: Maximum Product Subarray
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""


def maxProduct(nums):
    z = nums[0]
    pn,pp,cn,cp = z,z,z,z

    for i in nums[1:]:
        cp = max(pp*i, pn*i, i)
        cn = min(pp*i, pn*i, i)
        z = max(z, cp, cn)
        pp, pn = cp, cn
    
    return z



############################################################################################


#-- Pattern - 3

"""
0/1 Knapsack Algorithm

LeetCode Problems:
LeetCode 416: Partition Equal Subset Sum
LeetCode 494: Target Sum
LeetCode 1049. Last Stone Weight II
"""



"""
LeetCode 416: Partition Equal Subset Sum
Given an integer array nums, return true if you can partition the array into two subsets such 
that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


# Tabulation - Bottom Up Approach   
def canPartition(nums):
    l,n,s = nums, len(nums), sum(nums)
    if s&1:
        return False
    
    w=s//2
    dp = [[-1 for i in range(w+1)] for i in range(n+1)]
    ANS = False
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                dp[i][j] = 0
                continue
            
            if l[i-1] <= j:
                dp[i][j] = max( l[i-1] + dp[i-1][j-l[i-1]],
                                dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
            
    print(dp)        
    return dp[-1][-1]==w



#  Recursion + Memorization : Top-Down

def canPartition(nums):
    l,n,s = nums, len(nums), sum(nums)
    if s&1:
        return False
    
    w=s//2
    dp = [[-1 for i in range(w+1)] for i in range(n+1)]
    def Knap(l,w,n):
        if w==0 or n==0:
            return 0
        
        if dp[n][w]!=-1:
            return dp[n][w]
        
        if l[n-1] <= w:
            dp[n][w] = max(l[n-1]+Knap(l,w-l[n-1],n-1),
                        Knap(l,w,n-1))
            return dp[n][w]
        else:
            dp[n][w] = Knap(l,w,n-1)
            return dp[n][w]
    
    return w==Knap(l,w,n)



# Recursion Approach


# Tabulation : Bottom-Up + Memorization





"""
LeetCode 494: Target Sum

You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and 
then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the 
expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.


Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1
"""


# Recursion

def findTargetSumWays(nums, target):
    l = nums
    W=target
    n=len(l)


    def Knap(W, l, n):
        if n==0 and W==0:
            return 1
        
        if n==0 and W!=0:
            return 0
        
        return Knap(W-l[n-1], l, n-1) + Knap(W+l[n-1], l, n-1)
    
    return Knap(W, l, n)
        



# Tabulation Approach

def findTargetSumWays(nums, target):
    l = nums
    W=target
    n=len(l)
    d={}
    def Knap(W, l, n):
        if n==0 and W==0:
            return 1
        
        if n==0 and W!=0:
            return 0
        
        if (n,W) in d:
            return d[(n,W)]
        
        d[(n,W)] = Knap(W-l[n-1], l, n-1) + Knap(W+l[n-1], l, n-1)

        return d[(n,W)]

    
    return Knap(W, l, n)




"""
LeetCode 1049. Last Stone Weight II

You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones 
have weights x and y with x <= y. The result of this smash is:
If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.
Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.

Example 2:
Input: stones = [31,26,33,21,40]
Output: 5
"""



# Recursion

def lastStoneWeightII(stones):
    l=stones
    s=sum(l)
    n=len(l)
    w=s//2

    def Knap(w, l, n):
        if n==0 and w==0:
            return True
        
        if n==0 and w!=0:
            return False
        
        return Knap(w-l[n-1], l, n-1) or Knap(w, l, n-1)
    

    while w>=0:
        if Knap(w, l, n):
            return s-2*w
        
        w-=1
    
    return 0



# Recursion + Memorization with Dictionary stored values



def lastStoneWeightII(stones):
    l=stones
    n=len(l)
    s=sum(l)
    w=s//2

    d={}
    def Knap(w,l,n):
        if n==0 and w==0:
            return True
        
        if n==0 and w!=0:
            return False
        t=(n,w)
        if (n,w) in d:
            return d[(n,w)]
        elif w>=l[n-1]:
            d[(n,w)] = Knap(w-l[n-1],l,n-1) or Knap(w,l,n-1)
        else:
            d[(n,w)] = Knap(w,l,n-1)
        
        return d[(n,w)]
    
    

    while w>=0:
        if Knap(w,l,n):
            return s-2*w
        
        w-=1
    
    return 0



# Recursion + memorization with dp Array/Table, Top Down


def lastStoneWeightII(stones):
    l=stones
    n=len(l)
    s=sum(l)
    w=s//2

    dp=[[-1 for i in range(w+1)] for i in range(n+1)]
    
    def Knap(w,l,n):
        if n==0 and w==0:
            return True
        
        if n==0 and w!=0:
            return False

        if dp[n][w]!=-1:
            return dp[n][w]
        elif w>=l[n-1]:
            dp[n][w] = Knap(w-l[n-1],l,n-1) or Knap(w,l,n-1)
        else:
            dp[n][w] = Knap(w,l,n-1)
        
        return dp[n][w]
    
    

    while w>=0:
        if Knap(w,l,n):
            return s-2*w
        
        w-=1
    
    return 0





############################################################################################


#-- Pattern - 4

"""
Unbounded Knapsack

LeetCode Problems:
LeetCode 322: Coin Change
LeetCode 518: Coin Change 2
LeetCode 279. Perfect Squares
"""


"""
LeetCode 322: Coin Change
You are given an integer array coins representing coins of different denominations and an integer amount representing a 
total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by 
any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
"""



# Recursion

def coinChange(coins, amount):
    l=coins
    w=amount
    n=len(l)
    g=10**9+7

    def Knap(w,l,n):
        if w==0:
            return 0
        if n==0 and w!=0:
            return g
        
        if w>=l[n-1]:
            return min(1+Knap(w-l[n-1],l,n), Knap(w,l,n-1))
        else:
            return Knap(w,l,n-1)
    

    ans = Knap(w,l,n)
    if ans>=g:
        return -1
    
    return ans
        



# Recursion + Memorization

def coinChange(coins, amount):
    l=coins
    w=amount
    n=len(l)
    g=10**9+7

    dp = [[-1 for i in range(w+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if j==0:
                dp[i][j] = 0
            elif i==0:
                dp[i][j] = g
    def Knap(w,l,n):
        if w==0:
            return 0
        if n==0 and w!=0:
            return g
        if dp[n][w]!=-1:
            return dp[n][w]

        if w>=l[n-1]:
            t = min(1+Knap(w-l[n-1],l,n), Knap(w,l,n-1))
        else:
            t = Knap(w,l,n-1)
        
        dp[n][w] = t
        return t
    
    ans = Knap(w,l,n)
    #print(dp)
    if ans>=g:
        return -1
    
    return ans
        



# tabulation + Bottom-Up



def coinChange(coins, amount):
    l=coins
    w=amount
    n=len(l)
    g=10**9+7

    dp = [[-1 for i in range(w+1)] for i in range(n+1)]
    
    for i in range(n+1):
        for j in range(w+1):
            if j==0:
                dp[i][j] = 0
            elif i==0:
                dp[i][j] = g
            elif j>=l[i-1]:
                dp[i][j] = min(1+dp[i][j-l[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    
    #print(dp)
    if dp[-1][-1]>=g:
        return -1
    
    return dp[-1][-1]
    
    
        







"""
LeetCode 518: Coin Change 2

You are given an integer array coins representing coins of different denominations and an integer amount representing a 
total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination 
of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

 
Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1


Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.


Example 3:
Input: amount = 10, coins = [10]
Output: 1
"""


# Recursion

def change(amount, coins):
    w,l,n = amount, coins, len(coins)

    def Knap(w,l,n):
        if w==0:
            return 1
        elif n==0:
            return 0
        
        if w>=l[n-1]:
            return Knap(w-l[n-1], l, n) + Knap(w,l,n-1)
        else:
            return Knap(w,l,n-1)
    
    return Knap(w,l,n)




# Recursion + Memo

def change(amount, coins):
    w,l,n = amount, coins, len(coins)
    dp = [[-1 for i in range(w+1)] for i in range(n+1)]
    def Knap(w,l,n):
        if w==0:
            return 1
        elif n==0:
            return 0
        if dp[n][w]!=-1:
            return dp[n][w]
        
        if w>=l[n-1]:
            t = Knap(w-l[n-1], l, n) + Knap(w,l,n-1)
        else:
            t = Knap(w,l,n-1)
        
        dp[n][w] = t
        return t
    
    return Knap(w,l,n)





# Tabulation Bottom Up


def change(amount, coins):
    w,l,n = amount, coins, len(coins)
    dp = [[-1 for i in range(w+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if j==0:
                dp[i][j] = 1
                continue
            elif i==0:
                dp[i][j] = 0
                continue
    
            if j>=l[i-1]:
                dp[i][j] = dp[i][j-l[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
            
            
    return dp[-1][-1]








"""
LeetCode 279. Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product of some 
integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


# Recursion + Memorization

from math import *
def numSquares(n):
    w=n
    m=int(sqrt(n))
    g = 10**9+7
    dp = [[-1 for i in range(w+1)] for i in range(m+1)]
    def Knap(w,m):
        if w==0:
            return 0
        elif (m==0 and w!=0) or w<0:
            return g
        if dp[m][w]!=-1:
            return dp[m][w]

        if w>=(m*m):
            t = min(1+Knap(w-(m*m),m), Knap(w,m-1))
        else:
            t = Knap(w,m-1)
        
        dp[m][w] = t
        return t


    k=Knap(w,m)
    print(k)
    return k



#  Tabulation Bottom Up

from math import *
def numSquares(n):
    w=n
    m=int(sqrt(n))
    g = 10**9+7
    dp = [[-1 for i in range(w+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(w+1):
            if j==0:
                dp[i][j] = 0
            elif i==0:
                dp[i][j] = g

    for i in range(1,m+1):
        for j in range(1,w+1):

            if j>=(i*i):
                dp[i][j] = min(1+dp[i][j-(i*i)], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
            
    
    return dp[-1][-1]






############################################################################################


#-- Pattern - 5

"""
Longest Common Subsequence

LeetCode Problems:
LeetCode 1143: Longest Common Subsequence
LeetCode 583: Delete Operation for Two Strings
LeetCode 1092: Shortest Common Supersequence
"""



"""
LeetCode 1143: Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, 
return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted 
without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""



# Recursion


def longestCommonSubsequence(text1, text2):
    a,b = text1, text2
    m,n = len(a), len(b)

    def lcs(a,b,m,n):
        if m==0 or n==0:
            return 0
        
        if a[m-1]==b[n-1]:
            return 1+lcs(a,b,m-1,n-1)
        else:
            return max(lcs(a,b,m-1,n), lcs(a,b,m,n-1))
    
    return lcs(a,b,m,n)




# Recursion + memo


def longestCommonSubsequence(text1, text2):
    a,b = text1, text2
    m,n = len(a), len(b)
    dp = [[-1 for i in range(n+1)] for i in range(m+1)]
    def lcs(a,b,m,n):
        if m==0 or n==0:
            return 0
        if dp[m][n]!=-1:
            return dp[m][n]
        
        if a[m-1]==b[n-1]:
            t = 1+lcs(a,b,m-1,n-1)
        else:
            t = max(lcs(a,b,m-1,n), lcs(a,b,m,n-1))
        
        dp[m][n] = t
        return t
    
    return lcs(a,b,m,n)




# Tabulation Bottom Up


def longestCommonSubsequence(text1, text2):
    a,b = text1, text2
    m,n = len(a), len(b)
    dp = [[-1 for i in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = 0
                continue
            
            if a[i-1]==b[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
    
    return dp[-1][-1]





"""
LeetCode 583: Delete Operation for Two Strings
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.


Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4
"""



# Recursion

def minDistance(word1, word2):
    a,b = word1, word2
    m,n = len(a), len(b)

    def Knap(a,b,m,n):
        if m==0 or n==0:
            return m+n
        
        if a[m-1]==b[n-1]:
            return Knap(a,b,m-1,n-1)
        else:
            return 1+ min(Knap(a,b,m-1,n), Knap(a,b,m,n-1))
    
    return Knap(a,b,m,n)




# Recursion + Memorization

def minDistance(word1, word2):
    a,b = word1, word2
    m,n = len(a), len(b)
    dp = [[-1 for i in range(n+1)] for i in range(m+1)]

    def Knap(a,b,m,n):
        if m==0 or n==0:
            return m+n
        if dp[m][n]!=-1:
            return dp[m][n]

        if a[m-1]==b[n-1]:
            t = Knap(a,b,m-1,n-1)
        else:
            t = 1+ min(Knap(a,b,m-1,n), Knap(a,b,m,n-1))
        
        dp[m][n] = t
        return t
    
    return Knap(a,b,m,n)



# Tabulation Bottom Up

def minDistance(word1, word2):
    a,b = word1, word2
    m,n = len(a), len(b)
    dp = [[-1 for i in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = i+j
                continue

            if a[i-1]==b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+ min(dp[i-1][j], dp[i][j-1])
            
    
    return dp[-1][-1]



#   Solution - 2 for the above problem is Find LCS and return m+n-2*LCS
# A small example of the Solution is as follows

def minDistance(word1, word2):
    a,b = word1, word2
    m,n = len(a), len(b)
    dp = [[-1 for i in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = 0
                continue
            
            if a[i-1]==b[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
    
    return m+n-2*dp[-1][-1]     # Please check this last line which calculates the main logic of the answer



"""
LeetCode 1092: Shortest Common Supersequence

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. 
If there are multiple valid strings, return any of them.
A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 
Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
"""


# Tabulation Bottom Up

def shortestCommonSupersequence(str1, str2):
    a,b = str1, str2
    m,n = len(a), len(b)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    def String_length(a,b,m,n):

        for i in range(m+1):
            for j in range(n+1):

                if i==0:
                    dp[i][j] = j
                elif j==0:
                    dp[i][j] = i
                elif a[i-1]==b[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    z_len = String_length(a,b,m,n)
    z=''
    
    i,j = m,n
    while i>0 and j>0:
        if a[i-1]==b[j-1]:
            z = a[i-1]+z
            i-=1
            j-=1
        elif dp[i-1][j]<dp[i][j-1]:
            z = a[i-1] + z
            i-=1
        else:
            z = b[j-1] + z
            j-=1
    
    while i>0:
        z = a[i-1]+z
        i-=1
    
    while j>0:
        z = b[j-1] + z
        j-=1
    

    return z





############################################################################################


#-- Pattern - 6

"""
6. Longest Increasing Subsequence (LIS)

LeetCode Problems:
LeetCode 300: Longest Increasing Subsequence
LeetCode 673: Number of Longest Increasing Subsequence
leetCode 354: Russian Doll Envelopes
"""




"""
LeetCode 300: Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""



# Tabulation Bottom Up --- Optimized Solution

def lengthOfLIS(nums):
    l=nums
    n=len(l)
    dp=[1]*n

    for i in range(1,n):
        for j in range(i):
            if l[j]<l[i]:
                dp[i] = max(dp[i],1+dp[j])
    
    return max(dp)








"""
LeetCode 673: Number of Longest Increasing Subsequence

Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.


Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
"""

# Tabulation Bottom Up

def findNumberOfLIS(nums):
    l = nums
    n=len(l)
    dp = [1]*n
    cnt = [1]*n

    for i in range(1,n):
        for j in range(i):
            if l[j]<l[i] and dp[i]<(dp[j]+1):
                dp[i] = dp[j]+1
                cnt[i] = cnt[j]
            elif l[j]<l[i] and dp[i]==(dp[j]+1):
                cnt[i]+=cnt[j]
    
    lis = max(dp)
    z = 0
    for i in range(n):
        if dp[i]==lis:
            z+=cnt[i]
    
    return z
