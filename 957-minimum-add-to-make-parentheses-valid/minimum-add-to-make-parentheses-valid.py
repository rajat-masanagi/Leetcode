class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        top=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append('(')
                top+=1
            elif s[i]==')':
                if len(stack)==0 or stack[top-1]!='(':
                    stack.append(')')
                    top+=1
                else:
                    stack.pop()
                    top-=1
        print(stack)
        return len(stack)