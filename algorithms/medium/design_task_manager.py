from collections import defaultdict
from typing import List
from sortedcontainers import SortedList

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.sl = SortedList()
        for user_id, task_id, priority in tasks:
            self.sl.add((-priority, -task_id))
        self.hsh = defaultdict(list)
        for user_id, task_id, priority in tasks:
            self.hsh[task_id] = [user_id, priority]

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.sl.add((-priority, -taskId))
        self.hsh[taskId] = [userId, priority]

    def edit(self, taskId: int, newPriority: int) -> None:
        tpl = (-self.hsh[taskId][1], -taskId)
        i = self.sl.bisect_left(tpl)
        del self.sl[i]
        self.sl.add((-newPriority, -taskId))
        self.hsh[taskId][1] = newPriority

    def rmv(self, taskId: int) -> None:
        tpl = (-self.hsh[taskId][1], -taskId)
        i = self.sl.bisect_left(tpl)
        del self.sl[i]
        del self.hsh[taskId]

    def execTop(self) -> int:
        if len(self.sl) == 0:
            return -1
        priority, task_id = self.sl.pop(0)
        user_id, _ = self.hsh[-task_id]
        del self.hsh[-task_id]
        return user_id

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

# Main section
#  ['TaskManager','add','edit','execTop','rmv','add','execTop']
#  [[[[1,101,10],[2,102,20],[3,103,15]]],[4,104,5],[102,8],[],[101],[5,105,15],[]]

