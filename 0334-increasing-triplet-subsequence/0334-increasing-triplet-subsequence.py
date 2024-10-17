class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # for i in range(2,len(nums)):
        #     print(nums[i-2],nums[i-1],nums[i])
        #     if nums[i-2] < nums[i-1] < nums[i]:
        #         return True
        # return False
        num1 = float('inf')
        num2 = float('inf')

        for n in nums:
            if n <= num1:
                num1 = n
            elif n <= num2:
                num2 = n
            else:
                return True
        return False