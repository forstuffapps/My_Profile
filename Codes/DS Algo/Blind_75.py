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



"""
4. Product of Array Except Self  (LC number - 238)
"""
def productExceptSelf(nums):
    l=nums
    n=len(l)
    p=[1]*(n+2)
    r=[1]*(n+2)
    t=1
    for i in range(n):
        t*=l[i]
        p[i+1]=t
    t=1
    for i in range(n-1,-1,-1):
        t*=l[i]
        r[i+1]=t
    
    q=[]
    for i in range(1,n+1):
        q.append(p[i-1]*r[i+1])
    
    return q


# space optimised solution
def productExceptSelf(nums):
    n=len(nums)
    l=nums

    p=1
    s=1
    q=[1]*n

    for i in range(n):
        q[i]*=p
        p*=l[i]

        q[n-1-i]*=s
        s*=l[n-1-i]
    
    return q



"""
5. Maximum Subarray  (LC number - 53)
This is maximum subarray sum
"""

def maxSubArray(nums):
    i,j=0,0
    n=len(nums)
    l=nums
    c=l[0]
    m=c
    for i in range(1,n):
        c=max(l[i], c+l[i])
        m=max(m,c)
    return m



"""
6. Maximum Product Subarray  (LC number - 152)
"""

def maxProduct(nums):
    n=len(nums)
    l=nums
    pp,pn,cp,cn, z = l[0], l[0], l[0], l[0], l[0]

    for i in l[1:]:
        cp = max(pp*i, pn*i, i)
        cn = min(pp*i, pn*i, i)
        pp,pn = cp,cn
        z=max(z,cp,cn)
    
    return z



"""
7. Find Minimum in Rotated Sorted Array  (LC number - 153)
"""


def findMin(nums):
    l=nums
    n=len(l)
    if n==1:
        return l[0]
    lo,hi = 0,n-1
    z=l[0]
    while lo<=hi:
        m=(lo+hi)//2

        if l[0]<=l[m]:
            lo=m+1
        elif l[0]>l[m]:
            z=l[m]
            hi=m-1
        
        
    return z



# Another solution
def findMin(nums):
    l=nums
    n=len(l)
    lo,hi = 0,n-1
    while lo<hi:
        m=(lo+hi)//2
        if l[hi]<l[m]:
            lo=m+1
        else: 
            hi=m
        
    return l[lo]



"""
7. Search in Rotated Sorted Array  (LC number - 33)
"""



def search(nums, target):
    l=nums
    k=target
    n=len(l)
    
    lo,hi=0,n-1
    while lo<hi:
        m=(lo+hi)//2

        if l[m]<l[hi]:
            hi=m
        else:
            lo=m+1
    
    p=lo

    if l[-1]>=k:
        lo,hi=p,n-1
    else:
        lo,hi=0,p-1
    
    while lo<=hi:
        m=(lo+hi)//2

        if l[m]==k:
            return m
        elif l[m]<k:
            lo=m+1
        else:
            hi=m-1
        
    return -1



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
lower number of coins required to sum the final amount
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""

# Tabulation Bottom-Up Approach
def coinChange(coins, amount):
    l=coins
    m=len(l)
    n=amount
    g=10**9+7
    dp=[g]*(n+1)  # dp=[0]*(n+1) even this was accepted, g is for not possible cases
    dp[0]=0
    for i in range(1,n+1):
        k=g
        for j in range(m):
            if (i-l[j])>=0 and dp[i-l[j]]<g:  # there is a reason why we wrote <g not !=g cause dp[i] can be g+1 
                k=min(k,dp[i-l[j]])
        dp[i]=k+1
    print(dp)
    return -1 if dp[-1]>=g else dp[-1]


# Recursive
def coinChange(coins, amount):
    @lru_cache(maxsize=None)
    def z(coins, amount):
        A = amount
        l=coins
        n=len(l)
        g=10**9+7
        m=g

        if A<0:
            return g
        if A==0:
            return 0

        for i in range(n):
            m=min(m,z(l,A-l[i]))
        return m+1
    k=z(tuple(coins), amount)
    return -1 if k>=10**9+7 else k


# Tabulation : Bottom-Up    =>   Approach But using -1 as defualt value
def coinChange(coins, amount):
    l=coins
    m=len(l)
    n=amount
    dp=[-1]*(n+1)
    dp[0]=0
    g=10**9+7
    for i in range(1,n+1):
        k=g
        for j in range(m):
            q=(i-l[j])
            if q>=0 and dp[q]>=0:
                k=min(k,dp[q])
        
        if k<g:
            dp[i]=k+1
    
    return dp[-1]



"""
3. Longest Increasing Subsequence  (LC number - 300)
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
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
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
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
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
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




# another solution using g 
def wordBreak(s, wordDict):
        n=len(s)
        g=10**9+7
        dp=[g]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            for j in range(0,i):
                if dp[j]<g and s[j:i] in wordDict:
                    dp[i]=1 + dp[j]
                    
        return dp[-1]<g







"""
6. Combination Sum IV  (LC number - 377)

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
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

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
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
def rob(nums):
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
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
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
Goal : grid[0][0] -> grid[n-1][m-1]
actions : either i+1 or j+1 (move either down or right)
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

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""


def canJump(nums):
        
    n=len(nums)
    
    m=0

    for i in range(n):
        if i>m:
            return False
        m=max(m,i+nums[i])
    return True








#-- Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
1. Maximum Depth of Binary Tree
LC-104
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Input: root = [3,9,20,null,null,15,7]
Output: 3
"""


def maxDepth(root):
    def z(h):
        if h==None:
            return 0
        return 1+max(z(h.left) , z(h.right))
    
    return z(root)



"""
2. Same Tree
LC-100
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
"""


def isSameTree(p, q):
    def z(p,q):
        if p==None and q==None:
            return True
        elif p==None and q!=None:
            return False
        elif p!=None and q==None:
            return False
        
        return p.val==q.val and z(p.left,q.left) and z(p.right, q.right)
    
    return z(p,q)





"""
3. Invert Binary Tree
LC-226
Given the root of a binary tree, invert the tree, and return its root.
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""

def invertTree(root):
    def z(h):
        if h==None:
            return 
        
        z(h.left)
        z(h.right)
        t = h.left
        h.left = h.right
        h.right = t
        return h
    
    return z(root)



"""
4. Binary Tree Maximum Path Sum
LC-124
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
"""


def maxPathSum(root):
    g = 10**9+7
    ans = [-g]
    def z(h, ans):
        if h==None:
            return -g
        k = h.val
        k_left = z(h.left, ans)
        k_right = z(h.right, ans)
        q = max(k, k+k_left, k+k_right, k+k_left+k_right)
        ans[0] = max(ans[0],q)
        #print(ans, k)
        return max(k, k+k_left, k+k_right)
    
    z(root, ans)

    return ans[0]


"""
5. Binary Tree Level Order Traversal
LC-102
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""


def levelOrder(root):
    d={}
    def z(h,d, depth):
        if h==None:
            return d
        
        z(h.left,d, depth+1)
        try:
            d[depth].append(h.val)
        except:
            d.update({depth : [h.val]})
        z(h.right, d, depth+1)

        return d
    d = z(root,d,0)
    #print(len(d.keys()))
    n=len(d.keys())
    l=[]
    for i in range(n):
        l.append(d[i])
    
    return l




"""
7.Subtree of Another Tree
LC-572
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
"""

def compare(h1,h2):
    if h1==None and h2==None:
        return True
    elif h1!=None and h2!=None and h1.val==h2.val:
        return True and compare(h1.left,h2.left) and compare(h1.right, h2.right)
    else:
        return False

def isSubtree(root, subRoot):
    def check(r,s):
        if compare(r,s):
            return True
        elif r!=None:
            return check(r.left,s) or check(r.right,s)
        
        return False
    
    return check(root,subRoot)








"""
Merge Two Binary Trees
LC - 617
You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
Return the merged tree.
Note: The merging process must start from the root nodes of both trees.
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
"""


def mergeTrees(root1, root2):
    def z(h1,h2):
        if h1==None and h2==None:
            return h1,h2
        elif h1!=None and h2==None:
            return h1,h2
            #z(h1.left,h2)
            #z(h1.right, h2)
        elif h1==None and h2!=None:
            h1=TreeNode(h2.val)
            h1.left, h2.left = z(h1.left, h2.left)
            h1.right, h2.right = z(h1.right, h2.right)
            return h1,h2
        else:
            h1.val += h2.val
            h1.left, h2.left = z(h1.left, h2.left)
            h1.right, h2.right = z(h1.right, h2.right)
            return h1,h2
    
    root1, root2 = z(root1, root2)
    return root1
