class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2: # for length 0 & 1
            return len(nums)
        
        n_set = set(nums)
        max_len = 0

        for n in n_set:
            if n - 1 not in n_set:
                curr_num = n
                curr_len = 1

                while curr_num + 1 in n_set:
                    curr_num += 1
                    curr_len += 1

                max_len = max(max_len, curr_len)
        
        return max_len


        