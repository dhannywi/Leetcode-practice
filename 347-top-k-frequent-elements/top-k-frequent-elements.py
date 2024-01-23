class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using bucket sort
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # accounting for 0th index
        # [[],[],[], .... ,[]]

        for i in nums: # get count of each number
            count[i] = count.get(i, 0) + 1

        for n, c in count.items():
            freq[c].append(n) # add number n, at index c

        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result


