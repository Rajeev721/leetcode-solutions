class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count  = 0
        left, right = 0,len(nums) - 1
        nums.sort()
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                count += 1
                right -= 1
            if nums[left] + nums[right] < k:
                left += 1
            if nums[left] + nums[right] > k:
                right -= 1
        return count