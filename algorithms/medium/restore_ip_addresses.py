from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        st = set()
        def permute(s, seq):
            if s == '':
                seq = seq[:-1]
                if len(seq.split('.')) == 4:
                    valid = True
                    for x in seq.split('.'):
                        if int(x) > 255:
                            valid = False
                            break
                    if valid:
                        st.add(seq)
                return
            # s = '101023', seq = ''
            for i in range(1, 4):
                nextInt = s[:i]
                if len(nextInt) > 1 and nextInt[0] == '0':
                    continue
                chunk = s[i:]
                #permute(s[i:], seq+s[:i]+'.')
                permute(chunk, seq+nextInt+'.')
        seq = ''
        permute(s, seq)
        return list(st)

# Main section
for s in [
            '25525511135',
            '0000',
            '101023',
            '11111222221111122222',
            '11111111111111111111',
            '111111111111',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.restoreIpAddresses(s)
    print(f'r = {r}')
    print('===============')


