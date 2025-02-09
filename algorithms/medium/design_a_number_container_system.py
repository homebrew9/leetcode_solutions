from collections import defaultdict
from sortedcontainers import SortedList

class NumberContainers:
    def __init__(self):
        self.hindex = defaultdict(int)
        self.hint = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        if index in self.hindex:
            n = self.hindex[index]
            self.hint[n].remove(index)
            if len(self.hint[n]) == 0:
                del self.hint[n]
        self.hindex[index] = number
        self.hint[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.hint:
            return -1
        return self.hint[number][0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

# Main section
#  ["NumberContainers","find","change","change","change","change","find","change","find"]
#  [[],[10],[2,10],[1,10],[3,10],[5,10],[10],[1,20],[10]]
#  ["NumberContainers","change","find","change","find","find","find"]
#  [[],[1,10],[10],[1,20],[10],[20],[30]]

