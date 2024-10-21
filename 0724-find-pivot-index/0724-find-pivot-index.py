class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums = 0
        left_sum = 0
        for i in nums:
            sum_nums += i
        
        for i,j in enumerate(nums):
            if left_sum == (sum_nums - left_sum - j):
                return i
            left_sum += j
        return -1
        