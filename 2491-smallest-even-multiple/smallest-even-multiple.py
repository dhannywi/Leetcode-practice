class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # smallest multiple of 2 and n
        if n%2 == 0:
            return n
        else:
            return n*2
        