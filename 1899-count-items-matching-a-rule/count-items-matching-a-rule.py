class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        if ruleKey=="color":
            j=1
        elif ruleKey=="type":
            j=0
        elif ruleKey=="name":
            j=2
        for i in items:
            if i[j]==ruleValue:
                count=count+1
        return count