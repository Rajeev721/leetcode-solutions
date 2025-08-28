class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if intervals is None:
            return 0
        used_conf_rooms = 0
        number_of_meetings = len(intervals)

        start_intervals = sorted([i[0] for i in intervals])
        end_intervals = sorted([i[1] for i in intervals])
        start = end = 0
        while start < number_of_meetings:
            if start_intervals[start] >= end_intervals[end]:
                used_conf_rooms -= 1
                end += 1
            used_conf_rooms += 1
            start += 1
        return used_conf_rooms