from collections import defaultdict

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        hsh = defaultdict(int)
        for i, v in enumerate(s):
            hsh[v] = i
        seen = [0 for _ in range(26)]
        stack = list()
        orig = ord('a')
        for i, v in enumerate(s):
            if seen[ord(v) - orig] == 1:
                continue
            while len(stack) > 0 and stack[-1] > v and hsh[stack[-1]] > i:
                ch = stack.pop()
                seen[ord(ch) - orig] = 0
            stack.append(v)
            seen[ord(v) - orig] = 1
        res = ''
        while stack:
            res = stack.pop() + res
        return res

# Main section
for s in [
            'bcabc',
            'cbacdcbc',
            'rakbcfscthxjhzwotvsxxvhqrmzjutssjfcmtaqchnzqvmsjdhnjdnnhpvbqlzxyqwcnuigirhgafkodzouajzgqfpjthhlgvfoi',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.smallestSubsequence(s)
    print(f'r = {r}')
    print('===================================')





