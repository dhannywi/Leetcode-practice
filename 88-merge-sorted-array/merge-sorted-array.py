class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # loop over m+n times
        # tot = m+n
        # p1 = 0
        # p2 = 0
        # while i < tot and j < n:
        # # check if e1 < e2 or e1 = e2 -> move p1 +1
        # if 
        # # if e2 < e1 or e2 == 0, swap vals, move p1 +1
        # --- array slicing
        nums1[m:] = nums2[:]
        nums1.sort() 