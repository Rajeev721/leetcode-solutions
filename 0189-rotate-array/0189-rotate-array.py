class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        h = len(nums) - ( k % len(nums))

        a = nums[h:] + nums[:h]
        nums[:] = a