class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = maxL = 0
        for i in nums:
            if i == 1:
                curr += 1
            elif i == 0:
                curr = 0
            maxL = max(maxL, curr)
        return maxL