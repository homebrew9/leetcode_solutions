from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters)
        #print(f'\tlow, high = {low}, {high}')
        while low < high:
            mid = (low + high) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid
            #print(f'\t\tlow, mid, high = {low}, {mid}, {high}')
        #print(f'\tlow, high = {low}, {high}')
        if low >= len(letters):
            return letters[0]
        else:
            return letters[low]

# Main section
for letters, target in [
                          (['c','f','j'], 'a'),
                          (['c','f','j'], 'c'),
                          (['x','x','y','y'], 'z'),
                          (['x','x','x','y','z'], 'y'),
                          (['x','x','x','y','z'], 'x'),
                          (['m','m','n','q','r','r','t','x'], 'z'),
                          (['m','m','n','q','r','r','t','x'], 'o'),
                          (['m','m','n','q','r','r','t','x'], 'n'),
                          (['m','m','n','q','r','r','t','x'], 's'),
                          (['m','m','n','q','r','r','t','x'], 't'),
                          (['m','m','n','q','r','r','t','x'], 'x'),
                          (['m','m','n','q','r','r','t','x'], 'a'),
                       ]:
    print(f'letters, target = {letters}, {target}')
    sol = Solution()
    r = sol.nextGreatestLetter(letters, target)
    print(f'r = {r}')
    print('=======================')

