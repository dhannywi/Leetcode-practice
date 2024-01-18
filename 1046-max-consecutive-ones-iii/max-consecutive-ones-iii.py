class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # dynamic sliding window
        max_len = 0
        z_count = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                z_count += 1

            while z_count > k:
                if nums[l] == 0:
                    z_count -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len

