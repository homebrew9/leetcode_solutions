from collections import deque, defaultdict

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        if n <= 1:
            return 0
        rst = 0
        childs = defaultdict(list)
        for idx, parent in enumerate(manager):
            childs[parent].append(idx)
        print(f'\tchilds = {childs}')

        q = deque([(headID, informTime[headID])])
        print(f'\tq = {q}')
        while q:
            cur_id, cur_time = q.popleft()
            print(f'\t\tcur_id, cur_time = {cur_id}, {cur_time}')
            # calculate max
            rst = max(rst, cur_time)
            print(f'\t\trst = {rst}')
            for child in childs[cur_id]:
                q.append((child, cur_time + informTime[child]))
            print(f'\t\tq = {q}')
            print('=====')
        return rst

# Main section
for n, headID, manager, informTime in [
        (1, 0, [-1], [0]),
        (6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]),
        (9, 2, [2,2,-1,2,0,1,0,8,3], [2,3,1,5,0,0,0,0,3]),
        (11, 4, [5,9,6,10,-1,8,9,1,9,3,4], [0,213,0,253,686,170,975,0,261,309,337]),
        (11, 0, [-1,0,1,1,1,2,2,3,4,4,7], [1,2,4,10,2,0,0,1,0,0,0]),
    ]:
    print(f'n, headId, manager, informTime = {n}, {headID}, {manager}, {informTime}')
    sol = Solution()
    r = sol.numOfMinutes(n, headID, manager, informTime)
    print(f'r = {r}')
    print('=====================')

