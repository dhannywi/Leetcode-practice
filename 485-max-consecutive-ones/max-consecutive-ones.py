class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0

        return max(maxCount, count)