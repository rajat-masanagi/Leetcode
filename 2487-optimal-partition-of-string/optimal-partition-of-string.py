class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 0
        
        for char in s:
            if char not in seen:
                seen.add(char)
            else:
                seen = set(char)
                count += 1
        
        return count + 1 
