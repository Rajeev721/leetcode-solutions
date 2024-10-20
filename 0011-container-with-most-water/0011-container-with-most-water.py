class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0, len(height) - 1
        max_sum = 0

        while left < right:
            sum = min(height[left], height[right]) * (right-left)
            max_sum = max(sum, max_sum)
            if height[left] < height[right]:
                left += 1
            else: right -= 1
        return max_sum
            
        