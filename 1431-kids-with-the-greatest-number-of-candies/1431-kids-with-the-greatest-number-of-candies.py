class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolean_list = []
        max_value = 0
        for i in candies:
            if i > max_value:
                max_value = i
        for i in candies:
            if max_value <= i + extraCandies:
                boolean_list.append(True)
            else:
                boolean_list.append(False)
        return boolean_list