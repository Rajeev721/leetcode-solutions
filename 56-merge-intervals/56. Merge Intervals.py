class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        final_list = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i] == [0,0]:
                final_list.append(intervals[i])
                break
                
            if intervals[i][0] < intervals[i-1][0]:
                intervals[i-1][0] = intervals[i][0]
            
            if intervals[i][0] <= intervals[i-1][1] and intervals[i][1] >= intervals[i-1][1]:
                intervals[i-1][1] = intervals[i][1]
            if intervals[i][0] > intervals[i-1][0] and intervals[i][0] > intervals[i-1][1] and intervals[i][1] > intervals[i-1][1]:
                final_list.append(intervals[i])


        return final_list
