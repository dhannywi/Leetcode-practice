class Solution:
    # def runningSum(self, nums: List[int]) -> List[int]:
    #     running_sum = []
    #     for i in range(len(nums)):
    #         if i != 0:
    #             running_sum.append(nums[i]+ running_sum[i-1])
    #         else:
    #             running_sum.append(nums[i])
    #     return running_sum
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
