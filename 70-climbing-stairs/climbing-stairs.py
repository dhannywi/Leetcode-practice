class Solution:
    def climbStairs(self, n: int) -> int:
        # edge cases
        if n <= 3:
            return n
        
        memo = [0]*(n+1)
        memo[1:4] = [1, 2, 3]
        # now memo = [0, 1, 2, 3, 0*n-3 times]

        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]

        return memo[n]



        

