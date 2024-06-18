class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        for idx,ch in enumerate(s):
            d[ch]=idx
        start=0
        last_pos=0
        part_len=[]
        for idx,ch in enumerate(s):
            last_pos=max(last_pos,d[ch])
            if idx==last_pos:
                cl=last_pos - start +1
                part_len.append(cl)
                start=idx+1
        return part_len