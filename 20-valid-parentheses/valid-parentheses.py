class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if len(stack)==0:
                stack.append(i)
            elif i=='(' or i=='{' or i=='[':
                stack.append(i)
            elif i==')' and stack[-1]=='(':
                s=stack.pop()
            elif i==')' and stack[-1]!='(':
                stack.append(i)
            elif i=='}' and stack[-1]=='{':
                s=stack.pop()
            elif i=='}' and stack[-1]!='{':
                stack.append(i)
            elif i==']' and stack[-1]=='[':
                s=stack.pop()
            elif i==']' and stack[-1]!='[':
                stack.append(i)
        return len(stack)==0