sys.set_int_max_str_digits(10**6)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        st=""
        for i in num:
            st+=str(i)
        arr= int(st)+k
        res=[int(x) for x in str(arr)]
        return res