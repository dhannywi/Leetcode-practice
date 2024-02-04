class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
        res = [-1] * n
        window_size = k * 2 + 1

        if window_size > n:
            return res

        # prefix = [0]
        # for i in range(1, n):
        #     prefix.append(nums[i]+ prefix[-1])
        # return prefix # [0,4,7,16,17,25,30,32,38]

        prefix = [0]*(n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        # return prefix # [0,7,11,14,23,24,32,37,39,45]

        for i in range(k, n-k):
            res[i] = (prefix[i+k+1] - prefix[i-k])//window_size
        return res



        