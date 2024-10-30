class Solution:
    def rob(self, nums: List[int]) -> int:
        hashmap = {}
        rob1,rob2 = 0,0

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)-1):
            max_rob = max(rob1+nums[i], rob2)
            rob1,rob2 = rob2, max_rob
        hashmap["rob1"] = max_rob
        rob1,rob2 = 0,0
        for i in range(1, len(nums)):
            max_rob = max(rob1+nums[i], rob2)
            rob1,rob2 = rob2, max_rob
        hashmap["rob2"] = max_rob

        if hashmap["rob1"] > hashmap["rob2"]:
            return hashmap["rob1"]
        else:
            return hashmap["rob2"]