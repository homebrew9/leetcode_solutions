class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        def isInt(s):
            try:
                a = int(s)
            except:
                return False
            return True
        
        prev = None
        for word in s.split():
            if isInt(word):
                curr = int(word)
                if prev is None:
                    prev = curr
                elif curr <= prev:
                    return False
                else:
                    prev = curr
        return True

# Main section
for s in [
            '1 box has 3 blue 4 red 6 green and 12 yellow marbles',
            'hello world 5 x 5',
            'sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s',
            '1 2 3 4 5 6 7 8 9',
            '1 aaa 2 bbb ccc 3 ddd 4 eee 5 fff ggg 6 hhh 7 8 8',
         ]: 
    print(f's = {s}')
    sol = Solution()
    r = sol.areNumbersAscending(s)
    print(f'r = {r}')
    print('=========================')

