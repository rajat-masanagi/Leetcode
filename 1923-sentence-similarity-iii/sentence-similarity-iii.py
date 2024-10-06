class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        w1=sentence1.split()
        w2=sentence2.split()
        if len(w1)<len(w2):
            w1,w2=w2,w1
        start,end=0,0
        n1,n2=len(w1),len(w2)
        while start<n2 and w1[start]==w2[start]:
            start+=1
        while end<n2 and w1[n1-end-1]==w2[n2-end-1]:
            end+=1
        return start+end>=n2