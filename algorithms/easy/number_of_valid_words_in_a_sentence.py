class Solution:
    def countValidWords(self, sentence: str) -> int:
        digits = [str(i) for i in range(10)]
        punct = ['!','.',',']
        ans = 0
        for word in sentence.split():
            digit_found = False
            misplaced_hyphen = False
            multiple_or_misplaced_punct = False
            #print(word)
            for digit in digits:
                if digit in word:
                    digit_found = True
                    break
            if digit_found:
                continue
                
            if word.count('-') > 1 or word.startswith('-') or word.endswith('-'):
                continue
                
            for p in punct:
                if (p + '-' in word) or ('-' + p in word):
                    misplaced_hyphen = True
                    break
            if misplaced_hyphen:
                continue
                
            for p in punct:
                #print(f'p, word.find(p), len(word)-1 = {p}, {word.find(p)}, {len(word) - 1}')
                if word.count(p) > 1 or (word.find(p) >= 0 and word.find(p) != len(word) - 1):
                    multiple_or_misplaced_punct = True
                    break
            if multiple_or_misplaced_punct:
                continue
            ans += 1
        return ans

# Main section
for sentence in [
                   'cat and dog',
                   '!this  1-s b8d!',
                   'alice and  bob are playing stone-game10',
                ]:
    print(f'sentence = {sentence}')
    sol = Solution()
    r = sol.countValidWords(sentence)
    print(f'r = {r}')
    print('=================')

