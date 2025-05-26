from typing import List
from collections import defaultdict, Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        hsh = defaultdict(int)
        for word in words:
            hsh[word] += 1
        keys = list(hsh.keys())
        for k in keys:
            if k[0] == k[1]:
                v = hsh[k]
                if v % 2 == 0:
                    res += v * 2
                    del hsh[k]
                else:
                    res += (v - 1) * 2
                    hsh[k] = 1
            else:
                r = k[::-1]
                if r in hsh:
                    min_freq = min(hsh[k], hsh[r])
                    res += min_freq * 2 * 2
                    hsh[k] -= min_freq
                    if hsh[k] == 0:
                        del hsh[k]
                    hsh[r] -= min_freq
                    if hsh[r] == 0:
                        del hsh[r]
        # Check if a center can be set
        for k in hsh:
            if k[0] == k[1]:
                res += 2
                break
        return res
    def longestPalindrome_1(self, words: List[str]) -> int:
        seen = defaultdict(int)
        res = 0
        for i in words:
            reverse_i = i[1] + i[0]
            if seen[reverse_i] > 0:
                res += 4
                seen[reverse_i] -= 1
            else:
                seen[i] += 1
            #print(f'\t\ti, seen, res, res = {i}, {seen}, {res}')
        #print(f'\tseen = {seen}')
        for i in seen:
            if i[0] == i[1] and seen[i] > 0:
                res += 2
                break
        return res
    def longestPalindrome_2(self, words: List[str]) -> int:
        # a count variable contains the number of occurrences of each word
        count = Counter(words)
        answer = 0
        central = False
        for word, count_of_the_word in count.items():
            # if the word is a palindrome
            if word[0] == word[1]:
                if count_of_the_word % 2 == 0:
                    answer += count_of_the_word
                else:
                    answer += count_of_the_word - 1
                    central = True
            # consider a pair of non-palindrome words,
            # such that one is the reverse of another
            # word[1] + word[0] is the reversed word
            elif word[0] < word[1]:
                answer += 2 * min(count_of_the_word, count[word[1] + word[0]])
        if central:
            answer += 1
        return 2 * answer    

# Main section
for words in [
                ['lc','cl','gg'],
                ['ab','ty','yt','lc','cl','ab'],
                ['cc','ll','xx'],
                ['dd','aa','bb','dd','aa','dd','bb','dd','aa','cc','bb','cc','dd','cc'],
                ['nn','nn','hg','gn','nn','hh','gh','nn','nh','nh'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.longestPalindrome(words)
    r1 = sol.longestPalindrome_1(words)
    r2 = sol.longestPalindrome_2(words)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print('============================')

