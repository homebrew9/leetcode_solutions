"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict, deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hsh = defaultdict(list)
        for emp in employees:
            node, importance, subordinates = emp.id, emp.importance, emp.subordinates
            hsh[node] = [importance, subordinates]
        total_importance = 0
        dq = deque()
        seen = set()
        dq.append(id)
        seen.add(id)
        while dq:
            size = len(dq)
            for _ in range(size):
                curr = dq.popleft()
                total_importance += hsh[curr][0]
                for subordinate in hsh[curr][1]:
                    if subordinate not in seen:
                        dq.append(subordinate)
                        seen.add(subordinate)
        return total_importance


