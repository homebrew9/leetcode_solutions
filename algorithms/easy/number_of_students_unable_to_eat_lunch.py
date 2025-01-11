from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True:
            if len(students) == 0 and len(sandwiches) == 0:
                return 0
            if not sandwiches[0] in students:
                return len(students)
            if students[0] == sandwiches[0]:
                del students[0]
                del sandwiches[0]
            else:
                i = students[0]
                del students[0]
                students.append(i)
            print(f'\tstudents, sandwiches = {students}, {sandwiches}')
        return students

# Main section
for students, sandwiches in [
                               ([1,1,0,0], [0,1,0,1]),
                               ([1,1,1,0,0,1], [1,0,0,0,1,1]),
                               ([0,0,0], [1,0,0]),
                               ([0,1,0], [1,0,1]),
                               ([1,1,0,0,0,0,1,1,0,1], [0,0,1,1,1,0,0,1,0,1]),
                            ]:
    print(f'students = {students}')
    sol = Solution()
    r = sol.countStudents(students, sandwiches)
    print(f'r = {r}')
    print('==================')

