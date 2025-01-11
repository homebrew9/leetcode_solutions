class Solution:
    def minTimeToType(self, word: str) -> int:
        def minPath(c1, c2):
            # Function to return the minimum path from character c1 to c2
            # either clockwise or anti-clockwise
            forward = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
            reverse = 'zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba'
            i = forward.find(c1)
            j = forward.find(c2, i)
            fdist = abs(i - j)
            i = reverse.find(c1)
            j = reverse.find(c2, i)
            rdist = abs(i - j)
            return min(fdist, rdist)
        
        seconds = 0
        from_ch = 'a'
        for ch in word:
            temp = minPath(from_ch, ch)
            print(f'\tfrom_ch, ch, temp = {from_ch}, {ch}, {temp}')
            seconds += temp
            from_ch = ch
        seconds += len(word)
        return seconds

# Main section
for word in [
               'abc',
               'bza',
               'zjpc',
               'thequickbrownfoxjumpsoverthelazydog',
            ]:
    print(f'word = {word}')
    sol = Solution()
    r = sol.minTimeToType(word)
    print(f'r = {r}')
    print('================')

