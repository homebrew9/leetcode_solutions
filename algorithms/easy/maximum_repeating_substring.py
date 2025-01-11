#
# Sliding window approach does not work for last test case.
# The correct answer is 5 but this program returns 4.
# Trying brute force next.
#
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        curr, kvalue = 0, 0
        i = 0
        m = len(sequence)
        n = len(word)
        while True:
            if i + n > m:
                break
            if sequence[i:i+n] == word:
                curr += 1
                if curr > kvalue:
                    kvalue = curr
                i += n
            else:
                curr = 0
                i += 1
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

