class TwoSum:
    def __init__(self):
        self.nums = list()

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find(self, value: int) -> bool:
        if len(self.nums) < 2:
            return False
        seen = set()
        for i, v in enumerate(self.nums):
            if value - v in seen:
                return True
            seen.add(v)
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

# Main section
#  ["TwoSum","add","add","add","find","find"]
#  [[],[1],[3],[5],[4],[7]]

