class MyCalendar:

    def __init__(self):
        self.calendar=[]
        
    def book(self, start: int, end: int) -> bool:
        for i in self.calendar:
            if not (end <= i[0] or start >= i[1]):
                return False
        self.calendar.append([start,end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)