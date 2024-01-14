class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # check if ransomNote longer than magazine
        if len(ransomNote) > len(magazine):
            return False
        # store count of magizine character
        mg = {}
        for e in magazine:
            mg[e] = mg.get(e, 0) + 1
  
        # decrease count in mg if used for ransome note
        for i in ransomNote:
            if i not in mg or mg[i] == 0:
                return False
            else:
                mg[i] -= 1
        return True


# Solution using two dictionary

# from collections import Counter

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         # check if ransomNote longer than magazine
#         if len(ransomNote) > len(magazine):
#             return False
#         # store letters and its count time: O(m+n) space: O(m)
#         mag_count = Counter(magazine) # O(m)
#         rn_count = Counter(ransomNote) # O(n)

#         for key in rn_count.keys():
#             if key not in mag_count or mag_count[key] < rn_count[key]:
#                 return False
#         return True


