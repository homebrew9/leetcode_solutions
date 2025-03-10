#
# TC = O(N * Log(N)) ; SC = O(N). Binary Search.
#
from collections import defaultdict
class Solution:
    def maximumLength(self, s: str) -> int:
        def special_sub_maxlen(freq):
            # Given a frequency list of a character, what is the length of the
            # longest substring that occurs more than 3 times in the list?
            # Note that if the list is [3, 2, 1] then the substring length = 2
            # occurs 3 times in it: twice in length 3 and once in length 2.
            # 'ccc' => 'cc' occurs 2 times here
            # 'cc'  => 'cc' occurs 1 time here, so total = 3
            left, right = 1, N
            while left <= right:
                mid = (left + right) // 2
                val = sum([max(x + 1 - mid, 0) for x in freq])
                if val < 3:
                    right = mid - 1
                else:
                    left = mid + 1
            return right
        N = len(s)
        arr = [[] for _ in range(26)]
        i, j = 0, 0
        while j < N:
            if s[j] != s[i]:
                arr[ord(s[i]) - 97].append(j - i)
                i = j
            j += 1
        arr[ord(s[i]) - 97].append(j - i)
        res = -1
        for lst in arr:
            if len(lst) > 0:
                val = special_sub_maxlen(lst)
                if val > 0:
                    res = max(res, special_sub_maxlen(lst))
        return res

# Main section
for s in [
            'aaaa',
            'abcdef',
            'abcaba',
            'thlhjmtrxhycuicjnfpbjrviaydjuboptumxbmqqbjkpivdsqq',
            'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
            'aaaaaaaabbbbbbbbbccccccccccddddddddddddddddddddddd',
            'cccerrrecdcdccedecdcccddeeeddcdcddedccdceeedccecde',
            'eccdnmcnkl',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.maximumLength(s)
    print(f'r = {r}')
    print('====================')


