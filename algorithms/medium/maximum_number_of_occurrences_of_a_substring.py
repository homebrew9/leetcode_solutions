from collections import defaultdict, Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ''' Consider the substring 'abc' in s = 'abcabcabc'. Frequency of 'abc' = 3 = k.
        1)  Each substring of 'abc' (i.e. a, b, c, ab, bc) must also occur at least 3 times.
        2)  Also, if a substring of 'abc' occurs p times in s, then p >= k. So there is no point
            in determining the frequency of the larger substring. It can never exceed that of the
            shorter substring. In this example, we only have to find the occurrences of substring
            of size "minSize" that satisfy the given condition.
        3)  If a substring "abc" satisfies the given condition, then every substring of "abc" also
            satisfies the given condition (which is "no. of unique letters <= maxLetters")
        4)  In other words, the parameter "maxSize" is useless, and given just to confuse.
        5)  maxFreq('abcabcabc', 3, 1, 3) No need to check for substring 'abc' or 'ab'. Just check freq of a, b, c.
        6)  maxFreq('abcabcaba', 3, 1, 3) 'abc' occurs 2 times, but 'a' (which is a substring of 'abc') occurs 4 times.
        '''
        N = len(s)
        hsh = defaultdict(int)
        for i in range(0, N - minSize + 1):
            chunk = s[i:i+minSize]
            if len(Counter(chunk)) <= maxLetters:
                hsh[chunk] += 1
        if len(hsh) == 0:
            return 0
        return max(hsh.values())

# Main section
for s, maxLetters, minSize, maxSize in [
                                          ('aababcaab', 2, 3, 4),
                                          ('aaaa', 1, 3, 3),
                                          ('abcabcabcabc', 3, 3, 5),
                                       ]:
    print(f's, maxLetters, minSize, maxSize = {s}, {maxLetters}, {minSize}, {maxSize}')
    sol = Solution()
    r = sol.maxFreq(s, maxLetters, minSize, maxSize)
    print(f'r = {r}')
    print('========================')

