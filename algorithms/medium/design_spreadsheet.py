import re
class Spreadsheet:
    def __init__(self, rows: int):
        self.sheet = [[0 for _ in range(26)] for _ in range(rows + 1)]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:])
        self.sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:])
        self.sheet[row][col] = 0

    def getValue(self, formula: str) -> int:
        arr = re.split(r'[=+]', formula)
        left, right = arr[1], arr[2]
        if left[0].isdigit():
            val1 = int(left)
        else:
            col = ord(left[0]) - ord('A')
            row = int(left[1:])
            val1 = self.sheet[row][col]
        if right[0].isdigit():
            val2 = int(right)
        else:
            col = ord(right[0]) - ord('A')
            row = int(right[1:])
            val2 = self.sheet[row][col]
        return val1 + val2

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

# Test cases
#["Spreadsheet","getValue","setCell","getValue","setCell","getValue","resetCell","getValue"]
#[[3],["=5+7"],["A1",10],["=A1+6"],["B2",15],["=A1+B2"],["A1"],["=A1+B2"]]
#["Spreadsheet","setCell","resetCell"]
#[[24],["B24",66688],["O15"]]

