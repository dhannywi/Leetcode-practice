class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = 101
        for i in prices:
            if i < min1:
                min1, min2 = i, min1
            elif i < min2:
                min2 = i

        leftover = money - min1 - min2
        return leftover if leftover >= 0 else money


        '''
        # time: O(n logn) space: O(1)
        prices.sort()
        leftover = money - prices[0] - prices[1]
        return leftover if leftover >= 0 else money
        '''