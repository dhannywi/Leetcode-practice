class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
        res = [-1] * n
        window_size = k * 2 + 1

        if window_size > n:
            return res

        tally = sum(nums[:window_size])
        res[k] = tally // window_size

        # [-1,-1,-1,5,4,4,-1,-1,-1]
        for i in range(window_size, n):
            tally = tally - nums[i - window_size] + nums[i]
            res[i-k] = tally // window_size

        return res



         



        