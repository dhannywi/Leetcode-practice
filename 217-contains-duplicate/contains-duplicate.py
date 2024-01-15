class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n_set = set()
        for i in nums:
            if i not in n_set:
                n_set.add(i)
            else:
                return True
        return False