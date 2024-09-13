class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        if len(nums) <=1 :
            return 0
        
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
 
        while low < high:
            mid = (low + high)//2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid] < nums[mid - 1]:
                high = mid
            if nums[mid] < nums[mid + 1]:
                low = mid
        
        return -1