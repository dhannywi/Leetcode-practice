class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use bucket sort algorithm
        count = {}
        # build a frequency list of lists the size of nums + 1 (accounting for 0th index)
        freq = [[] for i in range(len(nums) + 1)]
        
        # count occurences
        for i in nums:
            count[i] = count.get(i, 0) +1

        # insert number n into frequency list at position c
        for n, c in count.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq)-1, 0, -1): # traverse frequency list from right to left
            for n in freq[i]: # append each elements in the list at index i
                result.append(n)
                if len(result) == k:
                    return result

        
