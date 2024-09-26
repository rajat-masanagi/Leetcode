class Solution:
    def isHappy(self, n: int) -> bool:
        hsh=set()
        while(True):
            z=0
            for i in str(n):
                z+=(int(i))**2
            if z==1:
                return True
            if z in hsh:
                return False
            else:
                hsh.add(z)
            n=z
        