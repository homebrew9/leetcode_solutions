class Solution:
    def canWinNim(self, n: int) -> bool:
        # n =  1 => true (I can win)
        # n =  2 => true (I can win)
        # n =  3 => true (I can win)
        # n =  4 => false (No way I can win if I start: 1-3, 2-2, 3-1)
        #           In general, the one who starts with 4 stones, loses.
        # n =  5 => true (I take 1, friend starts with 4 stones.)
        # n =  6 => true (I take 2, friend starts with 4 stones.)
        # n =  7 => true (I take 3, friend starts with 4 stones.)
        # n =  8 => false (I cannot take 4 stones; whatever I do, friend can make me start with 4 stones.)
        # n =  9 => true (I try to be the last person to clear away 5 stones, so that friend starts with 4 stones.
        #                 So 1-1-3, 1-2-2, or 1-3-1)
        # n = 10 => true (I try to be the last person to clear away 6 stones, so that friend starts with 4 stones.
        #                 So 2-1-3, 2-2-2, or 2-3-1)
        # Basically, I should take away n % 4 stones first in order to win. And this will not work if n is a 
        # multiple of 4.
        return n % 4 != 0

# Main section
sol = Solution()
for n in [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25
         ]:
    print(f'n = {n}')
    r = sol.canWinNim(n)
    print(f'r = {r}')
    print('===========================')


