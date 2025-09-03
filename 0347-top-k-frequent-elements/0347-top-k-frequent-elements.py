class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        nums_list = [[] * i for i in range(len(nums)+1)]


        for i in nums:
            hash_map[i] = 1 + hash_map.get(i,0)
        print(hash_map)        
        for num,val in hash_map.items():
            nums_list[val].append(num)
        result = []
        for i in range(len(nums_list)-1,0,-1):
            for n in nums_list[i]:
                result.append(n)
                if len(result) == k:
                    return result