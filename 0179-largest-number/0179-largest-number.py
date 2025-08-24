class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        list_map = sorted([str(i) for i in nums],key= lambda a: a* 10,  reverse=True)
        if list_map[0] == "0":
            return "0"
        return ''.join(list_map)