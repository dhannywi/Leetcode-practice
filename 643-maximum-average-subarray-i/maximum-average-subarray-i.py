class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # fixed sliding window of length k
        l = 0
        tot = sum(nums[:k])
        avg = tot/k
        max_avg = avg

        for r in range(k, len(nums)):
            tot += nums[r]
            tot -= nums[l]
            avg = tot/k
            max_avg = max(max_avg, avg)
            l += 1
            r += 1
        return max_avg


        