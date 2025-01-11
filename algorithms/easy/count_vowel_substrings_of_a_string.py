#
# Does not work for the last test case. This logic returns 68 substrings
# but there are 76 substrings total.
#
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = ['a','e','i','o','u']
        cnt = 0
        left, right = 0, 0
        in_block = False
        min_index = -1
        for right in range(len(word)):
            ch = word[right]
            if not ch in vowels:
                #print(left, right)
                for l in range(left+1, min_index+1):
                    for r in range(min_index+1, right+2):
                        #print(f'\t=>({l},{r}) ; chunk = {word[l:r]}')
                        if sorted(set(word[l:r])) == vowels:
                            print(f'\t=>({l},{r}) ; chunk = {word[l:r]}')
                            cnt += 1
                in_block = False
                left = right
            else:
                if not in_block:
                    in_block = True
                    left = right
                if sorted(set(word[left:right+1])) == vowels:
                    print(f'\t({left},{right}) ; => {word[left:right+1]}')
                    cnt += 1
                    if min_index == -1:
                        min_index = right
        print(f'left, right, min_index = {left}, {right}, {min_index}')
        for l in range(left+1, min_index+1):
            for r in range(min_index+1, right+2):
                #print(f'\t=>({l},{r}) ; chunk = {word[l:r]}')
                if sorted(set(word[l:r])) == vowels:
                    print(f'\t\t=>({l},{r}) ; chunk = {word[l:r]}')
                    cnt += 1
        return cnt

# Main section
for word in [
               #'aeiouua',
               #'unicornarihan',
               #'cuaieuouac',
               #'cuaieoxyz',
               #'xaeiouaeiy',
               #'xaeiouaaiy',
               #'poazaeuioauoiioaouuouaui',
               'ughspuuoaaaoieiuiaoiuee',
            ]:
    print(f'word = {word}')
    sol = Solution()
    r = sol.countVowelSubstrings(word)
    print(f'r = {r}')
    print('=====================')

