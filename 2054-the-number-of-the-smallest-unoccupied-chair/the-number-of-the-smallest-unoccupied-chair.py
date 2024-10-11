class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target=times[targetFriend]
        times.sort(key = lambda x: x[0])
        newtarget=times.index(target)
        open_chairs=[0]*len(times)
        for i in range(len(times)):
            for j in range(len(open_chairs)):
                if times[i][0]>=open_chairs[j]:
                    if i==newtarget:
                        return j
                    else:
                        open_chairs[j]=times[i][1]
                        break
            
        return len(times)-1