class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_dict = {}
        for ind,num in enumerate(nums):
            if target - num in final_dict:
                return [final_dict[target - num],ind]
            else:
                final_dict[num] = ind