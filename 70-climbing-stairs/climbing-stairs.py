class Solution:
    def climbStairs(self, n: int) -> int:
        # super optimized solution
        # time: O(n), space: O(1)
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        
        return b
        



        

