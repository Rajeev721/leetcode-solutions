class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # zeros = ones = twos = 0
        # for i in range(len(nums)):
        #     if nums[i] ==0:
        #         zeros +=1
        #     elif nums[i] == 1:
        #         ones += 1
        #     else:
        #         twos += 1
        # nums[:zeros] = [0] * zeros
        # nums[zeros:zeros+ones] = [1] * ones
        # nums[zeros+ones:] = [2] * twos
        low_value = mid_value = 0
        high_value = len(nums) - 1
        
        while mid_value <= high_value:
            if nums[mid_value] == 0:
                nums[mid_value], nums[low_value] = nums[low_value], nums[mid_value]
                low_value += 1
            elif nums[mid_value] == 2:
                nums[mid_value], nums[high_value] = nums[high_value], nums[mid_value]
                high_value -= 1
                mid_value -= 1
            mid_value += 1