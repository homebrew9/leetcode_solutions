class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # If k > 1, then we can swap any two adjacent characters.
        # abXYZ -> aXYZb -> XYZba -> YZbaX -> ZbaXY -> baXYZ
        # If we can swap adjacent characters, then we can swap any characters
        # in the string, thus completely sorting the string.
        # For k = 1, the best we can do is rotate the string character by
        # character and search for the lexicographically minimum one.
        if k > 1:
            return ''.join(sorted(s))
        else:
            return min(s[i:] + s[:i] for i in range(len(s)))

# Main section
for s, k in [
               ('cba', 1),
               ('edcba', 2),
               ('baaca', 3),
               ('bbcaacba', 3),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.orderlyQueue(s, k)
    print(f'r = {r}')
    print('===============')

