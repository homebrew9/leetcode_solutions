from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        st1 = set()
        st2 = set()
        hsh = dict()
        for person1, person2 in dislikes:
            print(f'\tperson1, person2 = {person1}, {person2}')
            group1, group2 = None, None
            if not person1 in hsh:
                st1.add(person1)
                hsh[person1] = 1
            else:
                group1 = hsh[person1]
            if not person2 in hsh:
                if group1 is None or group1 == 1:
                    st2.add(person2)
                    hsh[person2] = 2
                elif group1 == 2:
                    st1.add(person2)
                    hsh[person2] = 1
            else:
                group2 = hsh[person1]
            if group1 and group2 and group1 == group2:
                return False
            print(f'\tst1, st2 = {st1}, {st2}')
            print(f'\t=====')
        return True

# Main section
for n, dislikes in [
                      (10, [[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]]),
                   ]:
    print(f'n, dislikes = {n}, {dislikes}')
    sol = Solution()
    r = sol.possibleBipartition(n, dislikes)
    print(f'r = {r}')
    print('================')

