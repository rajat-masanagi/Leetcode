class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        L=[]
        for i in range(len(s)):
            y=startPos[0]
            x=startPos[1]
            count=0
            for j in s[i:]:
                if(j=='R'):
                    x=x+1
                elif(j=='L'):
                    x=x-1
                elif(j=="U"):
                    y=y-1
                elif(j=="D"):
                    y=y+1
                if y<0 or y>=n or x<0 or x>=n:
                    break
                elif y>=0 and y<n and x>=0 and x<n:
                    count=count+1
            L.append(count)
        return L
            