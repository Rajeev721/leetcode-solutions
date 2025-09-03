class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_freq_dict = {}

        k_freq_list = [[] * i for i in range (len(nums)+1)]

        for i in nums:
            k_freq_dict[i] = 1 + k_freq_dict.get(i,0)
        
        for key,val in k_freq_dict.items():
            k_freq_list[val].append(key)
        result = [k_freq_list[i] for i in range(len(k_freq_list)-1,0, -1)]
        return [ i for j in result for i in j][:k]
