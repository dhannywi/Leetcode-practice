class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        ans = 0
        for i in range(len(prefix) - 1):
            left = prefix[i]
            right = prefix[-1] - prefix[i]
            if left >= right:
                ans += 1
        
        return ans
