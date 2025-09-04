from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        def is_present(n):
            left, right = 0, N - 1
            while left <= right:
                mid = (left + right) // 2
                if friends[mid] == n:
                    return True
                if friends[mid] > n:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        N = len(friends)
        return [x for x in order if is_present(x)]
    def recoverOrder_1(self, order: List[int], friends: List[int]) -> List[int]:
        seen = set(friends)
        return [x for x in order if x in seen]

# Main section
for order, friends in [
                         ([3,1,2,5,4], [1,3,4]),
                         ([1,4,5,3,2], [2,5]),
                      ]:
    print(f'order   = {order}')
    print(f'friends = {friends}')
    sol = Solution()
    r = sol.recoverOrder(order, friends)
    r1 = sol.recoverOrder_1(order, friends)
    print(f'r       = {r}')
    print(f'r1      = {r1}')
    print('========================')

















