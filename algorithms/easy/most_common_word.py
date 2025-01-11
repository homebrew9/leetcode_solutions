#
# Does not work!! Either use regex or iterate through the paragraph char by char!!
#
from typing import List
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c,' ')
        paragraph = paragraph.lower()
        print(f'\t|{paragraph}|')
        for c in banned:
            paragraph = paragraph.replace(" "+c+" ", " ")
            paragraph = paragraph.replace(" "+c, " ")
            paragraph = paragraph.replace(c+" ", " ")
            paragraph = paragraph.replace(c, " ")
            #print(f'\t\tc = |{c}|')
            #if paragraph.find(" "+c+" ") >= 0:
            #    print(f'\t\t\tin if...')
            #    paragraph = paragraph.replace(" "+c+" ", " ")
            #    print(f'\t\t\t|{paragraph}|')
            #elif paragraph.find(" "+c) >= 0:
            #    print(f'\t\t\tin elif 1...')
            #    paragraph = paragraph.replace(" "+c, " ")
            #    print(f'\t\t\t|{paragraph}|')
            #elif paragraph.find(c+" ") >= 0:
            #    print(f'\t\t\tin elif 2...')
            #    paragraph = paragraph.replace(c+" ", " ")
            #    print(f'\t\t\t|{paragraph}|')
            #elif paragraph.find(c) >= 0:
            #    print(f'\t\t\tin elif 3...')
            #    paragraph = paragraph.replace(c, " ")
            #    print(f'\t\t\t|{paragraph}|')
        print(f'\t|{paragraph}|')
        arr = paragraph.split()
        cntr = Counter(arr)
        print(f'\t{cntr}')
        return cntr.most_common(1)[0][0]

# Main section
for paragraph, banned in [
                            #("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]),
                            #("a.", []),
                            #("the quick; brown, fox? jumps! over. the lazy' dog", ["quick","dog","fox"]),
                            #("the quick; brown, fox? a jumps! over. a the lazy' dog", ["the"]),
                            #("a, a, a, a, b,b,b,c, c", ["a"]),
                            ("abc abc? abcd the jeff!", ["abc","abcd","jeff"]),
                         ]:
    print(f'paragraph, banned = "{paragraph}", {banned}')
    sol = Solution()
    r = sol.mostCommonWord(paragraph, banned)
    print(f'r = {r}')
    print('=============================')

