class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split(' ')
        n=len(searchWord)
        for w in range(len(words)):
            m=len(words[w])
            if m<n:
                continue
            flag=0
            for i in range(n):
                if words[w][i]==searchWord[i]:
                    flag+=1
                else:
                    break
            if flag==n:
                return w+1

        return -1