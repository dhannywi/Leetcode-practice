from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # check if ransomNote longer than magazine
        if len(ransomNote) > len(magazine):
            return False
        # store letters and its count
        mag_count = Counter(magazine) # O(m)
        rn_count = Counter(ransomNote) # O(n)

        for key in rn_count.keys():
            if key not in mag_count or mag_count[key] < rn_count[key]:
                return False
        return True

