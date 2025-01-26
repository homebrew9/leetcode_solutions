from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        N = numberOfUsers
        priority = {'OFFLINE': 0, 'MESSAGE': 1}
        events = sorted(events, key=lambda x: (int(x[1]), priority[x[0]]))
        arr = [0 for _ in range(numberOfUsers)]
        mentions = [0 for _ in range(numberOfUsers)]
        for first, second, third in events:
            if first == 'OFFLINE':
                ts = int(second)
                ind = int(third)
                arr[ind] = ts + 60
            else:
                ts = int(second)
                for i, v in enumerate(arr):
                    if v > 0 and v < ts:
                        arr[i] = 0
                if third == 'ALL':
                    for i in range(N):
                        mentions[i] += 1
                elif third == 'HERE':
                    for i in range(N):
                        if arr[i] == 0 or arr[i] <= ts:
                            mentions[i] += 1
                else:
                    for idx in [int(item.replace('id','')) for item in third.split()]:
                        mentions[idx] += 1
        return mentions

# Main section
for numberOfUsers, events in [
                                (2, [['MESSAGE','10','id1 id0'],['OFFLINE','11','0'],['MESSAGE','71','HERE']]),
                                (2, [['MESSAGE','10','id1 id0'],['OFFLINE','11','0'],['MESSAGE','12','ALL']]),
                                (2, [['OFFLINE','10','0'],['MESSAGE','12','HERE']]),
                                (3, [['MESSAGE','2','HERE'],['OFFLINE','2','1'],['OFFLINE','1','0'],['MESSAGE','61','HERE']]),
                             ]:
    print(f'numberOfUsers, events = {numberOfUsers}, {events}')
    sol = Solution()
    r = sol.countMentions(numberOfUsers, events)
    print(f'r = {r}')
    print('======================')

