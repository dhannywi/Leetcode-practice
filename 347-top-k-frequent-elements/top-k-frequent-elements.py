class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_count = Counter(nums)

        sCount = dict(sorted(n_count.items(), key=lambda item: item[1], reverse=True))
        
        topk = list(sCount.keys())

        return topk[:k]