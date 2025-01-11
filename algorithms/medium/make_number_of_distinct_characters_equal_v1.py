from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cntr1 = Counter(word1)
        cntr2 = Counter(word2)
        keys1 = list(cntr1.keys())
        keys2 = list(cntr2.keys())
        for x in keys1:
            for y in keys2:
                # 1) Remove x from cntr1 and add to cntr2
                cntr1[x] -= 1
                cntr2[x] += 1
                # 2) Remove y from cntr2 and add to cntr1
                cntr2[y] -= 1
                cntr1[y] += 1

                if cntr1[x] == 0:
                    del cntr1[x]
                if cntr2[y] == 0:
                    del cntr2[y]

                #print(x, y, cntr1, cntr2)
                # If counter keys are identical then we are done
                if len(cntr1.keys()) == len(cntr2.keys()):
                    return True

                # Reverse of 1)
                cntr1[x] += 1
                cntr2[x] -= 1
                # Reverse of 2)
                cntr2[y] += 1
                cntr1[y] -= 1

                if cntr2[x] == 0:
                    del cntr2[x]
                if cntr1[y] == 0:
                    del cntr1[y]
        return False

# Main section
for word1, word2  in [
                        ('ac', 'b'),
                        ('abcc', 'aab'),
                        ('abcde', 'fghij'),
                        ('ab', 'abcc'),
                     ]:
    print(f'word1, word2 = {word1}, {word2}')
    sol = Solution()
    r = sol.isItPossible(word1, word2)
    print(f'r = {r}')
    print('=================')


