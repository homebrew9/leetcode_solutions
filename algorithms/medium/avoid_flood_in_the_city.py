from typing import List
from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        st = SortedList()
        mp = {}
        for i, rain in enumerate(rains):
            if rain == 0:
                st.add(i)
            else:
                ans[i] = -1
                if rain in mp:
                    it = st.bisect(mp[rain])
                    if it == len(st):
                        return []
                    ans[st[it]] = rain # type: ignore
                    st.discard(st[it])
                mp[rain] = i
        return ans

# Main section
for rains in [
                [1,2,3,4],
                [1,2,0,0,2,1],
                [1,2,0,1,2],
             ]:
    print(f'rains = {rains}')
    sol = Solution()
    r = sol.avoidFlood(rains)
    print(f'r = {r}')
    print('=====================')




























