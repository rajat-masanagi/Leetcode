class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s=""
        for i in s:
            if i.isalnum():
                filtered_s+=i.lower()
        n=len(filtered_s)
        j=n-1
        for i in range(n):
            if filtered_s[i]==filtered_s[j]:
                j-=1
                continue
            else:
                return False
        return True