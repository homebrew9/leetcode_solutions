from typing import List

class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.unalloc = set(range(maxNumbers))
        self.alloc = set()

    def get(self) -> int:
        if len(self.unalloc) == 0:
            return -1
        num = self.unalloc.pop()
        self.alloc.add(num)
        return num

    def check(self, number: int) -> bool:
        return number in self.unalloc

    def release(self, number: int) -> None:
        if number in self.alloc:
            self.alloc.remove(number)
            self.unalloc.add(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

# Main section
#['PhoneDirectory','get','get','check','get','check','release','check']
#[[3],[],[],[2],[],[2],[2],[2]]
#['PhoneDirectory','release','get']
#[[1],[0],[]]
#




