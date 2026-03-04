from typing import List

class Node:
    def __init__(self, val=0):
        self.val = val
        self.children = None
        self.valid = True
        self.parents = []

    def get_value(self):
        if self.children is None:
            return self.val
        if self.valid:
            return self.val
        
        result = 0
        for child in self.children: # type: ignore
            result += child.get_value()
        self.val = result
        self.valid = True
        return result

    def invalidate(self):
        self.valid = False

        for parent in self.parents:
            parent.invalidate()

class Excel:
    def __init__(self, height: int, width: str):
        int_width = self.convert_col(width)
        self.matrix = []

        for _ in range(height):
            row = []
            for _ in range(int_width+1):
                row.append(Node())
            self.matrix.append(row)
        self._print()

    def _print(self):
        for row in self.matrix:
            print("".join(str(col.get_value()) for col in row))
        
    def set(self, row: int, column: str, val: int) -> None:
        node = self.matrix[row-1][self.convert_col(column)]
        node.invalidate()
        node.val = val
        node.children = None

    def get(self, row: int, column: str) -> int:
        return self.matrix[row-1][self.convert_col(column)].get_value()

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        node = self.matrix[row-1][self.convert_col(column)]
        node.invalidate()

        node.children = []

        for s in numbers:
            #handle ranges
            if ":" in s:
                c1, r1 = s[0], int(s[1:s.index(":")])
                c2, r2 = s[s.index(":")+1], int(s[s.index(":") + 2 :])

                for i in range(r1-1, r2):
                    for j in range(self.convert_col(c1), self.convert_col(c2)+1):
                        node.children.append(self.matrix[i][j])
                        self.matrix[i][j].parents.append(node)
            else:
                c, r = s[0], int(s[1:])
                node.children.append(self.matrix[r-1][self.convert_col(c)])
                self.matrix[r-1][self.convert_col(c)].parents.append(node)
        self._print()
        return node.get_value()

    def convert_col(self, col):
        return ord(col) - ord('A')


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)

# Input data
#["Excel","set","sum","set","get"]
#[[3,"C"],[1,"A",2],[3,"C",["A1","A1:B2"]],[2,"B",2],[3,"C"]]












