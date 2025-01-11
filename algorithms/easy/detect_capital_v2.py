class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lc = [chr(i+97) for i in range(26)]
        uc = [chr(i+65) for i in range(26)]

        # All uppercase
        #print(f'All uppercase...')
        for i, c in enumerate(word):
            if c in lc:
                break
        if i == len(word) - 1 and c in uc:
            return True

        # All lowercase
        #print(f'All lowercase...')
        for i, c in enumerate(word):
            if c in uc:
                break
        if i == len(word) - 1 and c in lc:
            return True

        # Initcaps
        #print(f'Initcaps...')
        if word[0] in uc:
            for i, c in enumerate(word[1:]):
                #print(f'\t(i, c) = ({i}, {c})')
                if c in uc:
                    break
            #print(f'(i, c, len-2) = ({i}, {c}, {len(word)-2})')
            if i == len(word) - 2 and c in lc:
                return True
        return False

# Main section
for word in [
               'USA',
               'leetcode',
               'Google',
               'FlaG',
               'abcDefgHijkL',
               'HappyBirthday',
               'Happybirthday',
               'happybirthday',
               'HAPPYBIRTHDAY',
               'HAPPYBIRTHDAy',
               'happybirthdaY',
               'Fe',
               'a',
               'X',
               'aX',
            ]:
    print(f'word = {word}')
    sol = Solution()
    r = sol.detectCapitalUse(word)
    print(f'r = {r}')
    print('===========================')



