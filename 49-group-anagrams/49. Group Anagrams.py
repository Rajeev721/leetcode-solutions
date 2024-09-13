from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dict = defaultdict(list)
        for i in sorted(strs):
            final_dict[''.join((sorted(i)))].append(i)
        return final_dict.values()