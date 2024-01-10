class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_w = 0
        wealth = []
        for i in accounts:
            wealth.append(sum(i))
        return max(wealth)