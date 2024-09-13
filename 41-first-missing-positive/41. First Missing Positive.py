class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dict_nums = set(nums)
        min_value = 1
        while min_value in dict_nums:
            min_value += 1
        return min_value