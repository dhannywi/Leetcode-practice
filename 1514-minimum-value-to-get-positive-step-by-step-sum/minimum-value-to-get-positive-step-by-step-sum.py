class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startVal = 1
        tot = 0
        for i in nums:
            tot += i
            startVal = min(tot, startVal)
        if startVal > 0:
            return 1
        return abs(startVal) + 1        