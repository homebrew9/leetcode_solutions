from typing import List
from collections import defaultdict

class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        hsh = defaultdict(set)
        for s, b in students:
            hsh[b].add(s)
        return 0 if not hsh else max([len(v) for v in hsh.values()])

# Main section
for students in [
                   [[1,2],[2,2],[3,3],[1,3],[2,3]],
                   [[1,1],[2,1],[3,1],[4,2],[5,2]],
                   [[1,1],[1,1]],
                   [],
                ]:
    print(f'students = {students}')
    sol = Solution()
    r = sol.maxStudentsOnBench(students)
    print(f'r = {r}')
    print('===============================')

