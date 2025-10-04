from collections import defaultdict

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        hsh = defaultdict(int)
        for ch in s:
            hsh[ch] += 1
        hsh1 = defaultdict(set)
        for k, v in hsh.items():
            hsh1[v].add(k)
        arr = sorted([(list(v), k) for k, v in hsh1.items()], key=lambda x: (-len(x[0]), -x[1]))
        return ''.join(arr[0][0])

# Main section
for s in [
            'aaabbbccdddde',
            'abcd',
            'pfpfgi',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.majorityFrequencyGroup(s)
    print(f'r = {r}')
    print('==========================')


























