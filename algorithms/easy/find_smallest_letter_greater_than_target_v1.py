#
# Old code. This does not use Binary Search. Time complexity = O(N)
# The other Python script uses Binary Search; time complexity = O(log(N))
#
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for ch in letters:
            if target < ch:
                return ch
        return letters[0]

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

