class Solution:
    #def minimumPartition(self, s: str, k: int) -> int:
    #    # Iterating through s from left to right
    #    res = list()
    #    curr = ''
    #    for ch in s:
    #        if int(ch) > k:
    #            return -1
    #        else:
    #            curr += ch
    #            if int(curr) > k:
    #                res.append(curr[:-1])
    #                curr = curr[-1]
    #    if len(curr) > 0:
    #        res.append(curr)
    #    #print(res)
    #    return len(res)

    def minimumPartition(self, s: str, k: int) -> int:
        # Iterating through s from right to left
        res = list()
        curr = ''
        for ch in s[::-1]:
            if int(ch) > k:
                return -1
            else:
                curr = ch + curr
                if int(curr) > k:
                    res.append(curr[1:])
                    curr = curr[0]
        if len(curr) > 0:
            res.append(curr)
        #print(res)
        return len(res)

# Main section
for s, k in [
               ('165462', 60),
               ('238182', 5),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.minimumPartition(s, k)
    print(f'r = {r}')
    print('================')

