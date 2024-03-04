class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in num_dict:
                num_dict[n] = i
            else:
                return [i, num_dict[diff]]
