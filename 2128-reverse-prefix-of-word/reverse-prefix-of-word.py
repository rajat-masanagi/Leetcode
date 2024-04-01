class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if(ch in word):
            t=""
            for i in range(len(word)):
                t=t+word[i]
                if(word[i]==ch):
                    break
            return t[::-1]+word[i+1:]
        else:
            return word
                
