class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        l, r = 0, len(nums)-1
        while l <= r: # appends largest value first
            if nums[l]**2 > nums[r]**2:
                ans.append(nums[l]**2)
                l += 1
            else:
                ans.append(nums[r]**2)
                r -= 1

        return ans[::-1] # reverse resulting array to ascending order
        