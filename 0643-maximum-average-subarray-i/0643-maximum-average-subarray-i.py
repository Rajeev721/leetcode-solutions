class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k and k == 1:
            return nums[0]
        sum_val = sum(nums[:k])
        max_sum = sum_val
        j = 0
        for i in range(k,len(nums)):
            sum_val  -= nums[j]
            sum_val += nums[i]
            j += 1
            max_sum = max(max_sum, sum_val)      
        return max_sum/k
