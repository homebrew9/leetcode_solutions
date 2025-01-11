class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        def repeatSubstring(s, t):
            # Given a string "s" and substring "t", return the total
            # count of repetitions of "t" in "s" starting from index 0.
            cnt = 0
            i = 0
            n = len(t)
            while True:
                if i + n > len(s):
                    break
                if s[i:i+n] == t:
                    cnt += 1
                    i += n
                else:
                    break
            return cnt

        kvalue = 0
        for i in range(0, len(sequence)):
            curr = repeatSubstring(sequence[i:], word)
            if curr > kvalue:
                kvalue = curr
        return kvalue

# Main section
for sequence, word in [
                         ('ababc', 'ab'),
                         ('ababc', 'ba'),
                         ('ababc', 'ac'),
                         ('ababcdefabxyzabababpqrlmnab', 'ab'),
                         ('ababababababababababababababxababababababababababy', 'ab'),
                         ('abcabc', 'abc'),
                         ('a', 'a'),
                         ('aaabaaaabaaabaaaabaaaabaaaabaaaaba', 'aaaba'),
                      ]:
    print(f'sequence, word = {sequence}, {word}')
    sol = Solution()
    r = sol.maxRepeating(sequence, word)
    print(f'r = {r}')
    print('===================')


