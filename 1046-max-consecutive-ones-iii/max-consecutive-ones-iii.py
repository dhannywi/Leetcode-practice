class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        flip = 0
        maxL = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                flip += 1
            while flip > k:
                if nums[l] == 0:
                    flip -= 1
                l += 1
            maxL = max(maxL, r-l+1)
        return maxL

