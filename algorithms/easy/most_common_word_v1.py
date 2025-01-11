from typing import List
from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #for c in "!?',;.":
        #    paragraph = paragraph.replace(c,' ')
        paragraph = re.sub(r"[!?',;.]", " ", paragraph)
        paragraph = paragraph.lower()
        #print(f'\t|{paragraph}|')
        for c in banned:
            word = r"\b"+c+r"\b"
            paragraph = re.sub(word, " ", paragraph)
        #print(f'\t|{paragraph}|')
        arr = paragraph.split()
        cntr = Counter(arr)
        #print(f'\t{cntr}')
        return cntr.most_common(1)[0][0]

# Main section
for paragraph, banned in [
                            ("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]),
                            ("a.", []),
                            ("the quick; brown, fox? jumps! over. the lazy' dog", ["quick","dog","fox"]),
                            ("the quick; brown, fox? a jumps! over. a the lazy' dog", ["the"]),
                            ("a, a, a, a, b,b,b,c, c", ["a"]),
                            ("abc abc? abcd the jeff!", ["abc","abcd","jeff"]),
                         ]:
    print(f'paragraph, banned = "{paragraph}", {banned}')
    sol = Solution()
    r = sol.mostCommonWord(paragraph, banned)
    print(f'r = {r}')
    print('=============================')


