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
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
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
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
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
A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
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





