class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > res:
                res = area
            # compare pointer val, and update pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


                    
        


        