class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # smallest multiple of 2 and n
        return n if n%2==0 else n*2
        