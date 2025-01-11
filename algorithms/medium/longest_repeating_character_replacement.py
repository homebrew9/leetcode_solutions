#
# Ref: https://leetcode.com/problems/longest-repeating-character-replacement/discuss/765776/Python%3A-Two-Pointers-%2B-Process-for-coding-interviews
# Intuition:
# - Scan the array with 2 pointers: left and right
# - Store the frequency of each character
# - Compute the replacement cost: cells count between left and right pointers - the highest frequency
# - if the replacement cost <= k: update longest string size
# - if the replacement cost > k: decrease frequency of character at left pointer; increase left pointer and repeat
#
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        c_freq = {}
        longest_strlen = 0
        for r in range(len(s)):
            if not s[r] in c_freq:
                c_freq[s[r]] = 0
            c_freq[s[r]] += 1

            # Replacement cost = cell count between l and r minus highest freq
            cell_count = r - l + 1
            if cell_count - max(c_freq.values()) <= k:
                longest_strlen = max(longest_strlen, cell_count)
            else:
                c_freq[s[l]] -= 1
                if not c_freq[s[l]]:
                    c_freq.pop(s[l])
                l += 1
        return longest_strlen

# Main section
for s, k in [
               ('ABAB', 2),
               ('AABABBA', 1),
               ('BAAAABBA', 1),
               ('BAAAABBA', 3),
               ('BAAAABBBBBA', 1),
               ('CBAAAABBBBBA', 2),
               ('CBAAAABBBBBA', 1),
               ('CABAAAABBBBBA', 2),
            ]:
    print(f's, = {s}, {k}')
    sol = Solution()
    r = sol.characterReplacement(s, k)
    print(f'r = {r}')
    print('==========================')

