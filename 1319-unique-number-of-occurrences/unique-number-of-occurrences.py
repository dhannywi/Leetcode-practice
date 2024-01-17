class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # create dict with count O(n)
        freq = Counter(arr)

        return len(freq) == len(set(freq.values()))
            