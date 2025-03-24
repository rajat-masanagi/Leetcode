class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count=0
        new_meetings=[]
        for meeting in meetings:
            if not new_meetings or meeting[0] > new_meetings[-1][1]:
                new_meetings.append(meeting)
            else:
                new_meetings[-1][1] = max(new_meetings[-1][1], meeting[1])

        for s,e in new_meetings:
            count+=e-s+1
        return days-count