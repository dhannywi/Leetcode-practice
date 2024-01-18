class Solution:
    def climbStairs(self, n: int) -> int:
        # super optimized solution
        # time: O(n), space: O(1)
        if n <= 3:
            return n
            
        a = 1
        b = 2
        for i in range(2, n+1):
            b, a = b + a, b 
        return a
        



        

