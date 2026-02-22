from collections import Counter, deque
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            # Same characters are at least distance 0 apart, which means
            # any arrangement is valid, including the original string.
            return s
        N = len(s)
        cntr = Counter(s)
        # Max heap has characters in decreasing frequencies
        h = list()
        heapq.heapify(h)
        for key, val in cntr.items():
            heapq.heappush(h, (-val, key))
        # Deque is for holding characters with a "next index" tag
        # Each deque element = (next_index, char, freq)
        dq = deque()
        res = ['' for _ in range(N)]
        for i in range(N):
            # If the current index is one where the first deque character
            # should be placed, then move that character back to heap.
            if dq and dq[0][0] == i:
                next_idx, ch, cnt = dq.popleft()
                heapq.heappush(h, (-cnt, ch))
            # If heap is empty, we have nothing to work with. Impossible case.
            if len(h) == 0:
                return ''
            freq, c = heapq.heappop(h)
            freq = -freq
            res[i] = c
            freq -= 1
            # Only add to deque if there is a character to add
            # and an index to add to!
            if freq > 0 and i+k < N:
                dq.append((i+k, c, freq))
        return ''.join(res)

# Main section
for s, k in [
               ('aabbcc', 3),
               ('aaabc', 3),
               ('aaadbbcc', 2),
               ('aabbcc', 2),
               ('aabbcc', 1),
               ('aabbcc', 0),
               ('vlaisyodzkspqcprfhmilwdohtrskrscasjhkgwvjvwzziyjwcgqnkkpqvnivksethzzzmpepnywrhzuokzkfmmhrsspyrkttvzm', 11),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.rearrangeString(s, k)
    print(f'r = {r}')
    print('=================================================')
 



















