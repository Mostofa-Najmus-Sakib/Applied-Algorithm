"""
LeetCode Problem: 70. Climbing stairs
Link: https://leetcode.com/problems/climbing-stairs/
Language: Python
Written by: Mostofa Adib Shakib

"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 1
        
        dp = [0 for x in range(n)]
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]