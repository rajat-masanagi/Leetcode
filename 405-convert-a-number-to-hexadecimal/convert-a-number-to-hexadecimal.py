class Solution:
    def toHex(self, num: int) -> str:
        temp=abs(num)
        ans=''
        if num==0:
            return "0"
        if num<0:
            temp=2**32-temp
        while(temp!=0):
            r=temp%16
            if r<10:
                ans=str(r)+ans
            else:
                ans=chr(r-10+97)+ans
            temp=temp//16

        return ans