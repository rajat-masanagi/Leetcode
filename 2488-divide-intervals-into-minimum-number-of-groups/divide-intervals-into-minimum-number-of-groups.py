class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        group=0
        end_ptr=0
        for i in start_times:
            if i>end_times[end_ptr]:
                end_ptr+=1
            else:
                group+=1
        return group