from typing import List

class Solution:
    #def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    #    s = ''.join([str(i) for i in flowerbed])
    #    if s.startswith('00'):
    #        n -= 1
    #        s = s[2:]
    #    if n == 0:
    #        return True
    #    if len(s) == 0:
    #        return False
    #    if s.endswith('00'):
    #        n -= 1
    #        s = s[:-2]
    #    if n == 0:
    #        return True
    #    if len(s) == 0:
    #        return False
    #    zeros = '0'*(2*n+1)
    #    if s.find(zeros) < 0:
    #        return False
    #    return True

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        size = len(flowerbed)
        if size == 1:
            if flowerbed[0] == 1:
                return False
            elif flowerbed[0] == 0:
                if n == 1:
                    return True
                else:
                    return False
        i = 0
        while True:
            print(f'i, fb[i], n = {i}, {flowerbed[i]}, {n}')
            # At the start of list
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
                    i = min(i+2, size-1)
                else:
                    i += 1
            # At the end of list
            elif i == size - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
                break
            # In the middle of the list
            else:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
                i += 1
            print(f'\tfb = {flowerbed}')
        if n > 0:
            return False
        else:
            return True

# Main section
for flowerbed, n in [
                       #([1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,0,0], 3),
                       #([1,0,0,0,1], 1),
                       #([0,0,0], 1),
                       #([0,0,0], 2),
                       #([0,0,0], 3),
                       #([1], 0),
                       #([1,0,1], 0),
                       #([0], 1),
                       #([1], 1),
                       ([0,0], 2),
                    ]:
    print(f'flowerbed = {flowerbed}, n = {n}')
    sol = Solution()
    r = sol.canPlaceFlowers(flowerbed, n)
    print(f'r = {r}')
    print('==========================')

