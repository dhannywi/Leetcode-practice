class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        # map num as key, pos as val
        for i, n in enumerate(nums):
            # check value b4 adding to dict
            diff = target - n
            if diff in numMap:
                return [numMap[diff], i]
            else:
                numMap[n] = i
        
