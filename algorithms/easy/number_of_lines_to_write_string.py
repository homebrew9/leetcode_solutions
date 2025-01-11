from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total = 0
        count = 0
        arr = [widths[ord(i)-97] for i in s]
        for i in arr:
            if total + i <= 100:
                total += i
            else:
                count += 1
                total = i
        return [count+1, total]

# Main section
for widths, s in [
                    ([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 'abcdefghijklmnopqrstuvwxyz'),
                    ([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 'bbbcccdddaaa'),
                    ([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 'aaaaaaaaaabbbbbbbbbb'),
                    ([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 'aaaaaaaaaa'),
                    ([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 'a'),
                 ]:
    print(f'widths, s = {widths}, {s}')
    sol = Solution()
    r = sol.numberOfLines(widths, s)
    print(f'r = {r}')
    print('=============================')

