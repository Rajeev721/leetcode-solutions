class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        a = []
        idx = 0

        if len(nums) == 0:
                return [[lower, upper]]
        
        if lower < nums[0]:
            a.append([lower, nums[0] - 1])
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]+1:
                a.append([nums[i-1]+1, nums[i]-1])
            idx += 1
        if nums[idx] < upper:
            a.append([nums[idx]+1, upper])
        return a