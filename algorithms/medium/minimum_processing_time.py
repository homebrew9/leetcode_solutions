from typing import List

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        # Intuition: if a processor is available late, it should be assigned the tasks that complete faster.
        # And if a processor is available earlier, then it should be assigned the tasks that are slower.
        # For example, if processorTime = [8,10] and tasks=[4,1] then
        # we should assign 4 to 8 and 1 to 10, so that 8+4=12 and 10+1=11 and completion time is 12.
        # If we had assigned 4 to 10 and 1 to 8, then 10+4=14, 8+1=9 => completion time is 14.
        # The same logic can be extended to more than 2 processors. In this problem, sort the processorTime
        # in descending order, sort tasks in ascending order and assign "chunks" of 4 tasks per processor.
        # Find max time per processor and max time overall. That's the answer.
        processorTime.sort(reverse=True)
        tasks.sort()
        res = float('-inf')
        for i, p in enumerate(processorTime):
            # The "chunk" of tasks array corresponding to:
            # i = 0 is tasks[0:4]
            # i = 1 is tasks[4:8]
            # i = 2 is tasks[8:12] ... we can iterate through it as well.
            res = max(res, p + max(tasks[4*i:4*(i+1)]))
        return res

# Main section
for processorTime, tasks in [
                               ([8,10], [2,2,3,1,8,7,4,5]),
                               ([10,20], [2,3,1,2,5,8,4,3]),
                               ([3,4,5], [1,2,2,3,3,3,4,4,1,2,3,1]),
                               ([12,20,3,8,15,7,15,8,12,3,16,6,15,8,20,18,5,6,7,2,10,9,18,6,13], [143,112,202,15,171,120,82,15,21,179,149,84,96,114,93,55,217,197,176,12,102,130,44,216,71,26,151,93,96,186,206,111,205,135,60,152,105,149,230,6,226,107,175,80,21,196,177,3,51,27,235,115,131,122,56,97,115,204,17,221,120,220,124,64,113,76,8,31,143,23,116,99,224,54,31,22,53,234,105,119,221,187,224,39,238,3,116,91,184,233,15,41,190,131,25,108,244,97,52,183]),
                            ]:
    print(f'processorTime, tasks = {processorTime}, {tasks}')
    sol = Solution()
    r = sol.minProcessingTime(processorTime, tasks)
    print(f'r = {r}')
    print('================')

