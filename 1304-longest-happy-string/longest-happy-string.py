import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h=[]
        if a>0:
            heappush(h,(-a,'a'))
        if b>0:
            heappush(h,(-b,'b'))
        if c>0:
            heappush(h,(-c,'c'))  
        print(h)
        ans=''
        while h:
            z=heappop(h)
            if len(ans)>=2 and ans[-1]==ans[-2]==z[1]:
                if not h:
                    break
                y=heappop(h)
                ans+=y[1]
                if y[0]+1<0:
                    heapq.heappush(h,(y[0]+1,y[1])) #Subtract 1
                heapq.heappush(h,(z[0],z[1]))
            else:
                ans+=z[1]
                if z[0]+1<0:
                    heapq.heappush(h,(z[0]+1,z[1]))
        
        return ans

            
                
        print(l)
        return ans