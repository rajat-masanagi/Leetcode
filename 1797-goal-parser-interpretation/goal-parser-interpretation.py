class Solution:
    def interpret(self, command: str) -> str:
        st=command.replace("(al)","al")
        ss=st.replace("()","o")
        return ss