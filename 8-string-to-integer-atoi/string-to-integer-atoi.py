class Solution:
    def myAtoi(self, s: str) -> int:
        ans=0
        clean=""
        clean_len=0
        flag=0
        sign=1
        s=s.strip()
        for i in s:
            if i==" ":
                break
            elif i=='-':
                if flag==1:
                    break
                if clean_len==0:
                    sign=-1
                    flag=1
                else:
                    break
            elif i=='+':
                if flag==1:
                    break
                if clean_len==0:
                    sign=1
                    flag=1
                else:
                    break
            elif i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0':
                clean+=i
                clean_len+=1
            elif i.isalpha() or i=='.':
                break
        print(clean)
        if len(clean)==0:
            return 0
        ans= sign*int(clean)
        if ans>=2**31-1:
            return 2**31-1
        elif ans<=-2**31:
            return -2**31
        else:
            return ans
