class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s=['0']
        for i in range(1,n):
            rev=s[::-1]
            s.append('1')
            for j in range(len(rev)):
                if rev[j]=='1':
                    rev[j]='0'
                else:
                    rev[j]='1'
            s.extend(rev)

        return s[k-1]
            
