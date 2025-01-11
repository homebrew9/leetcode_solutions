from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def processLine(chunks, spaces):
            if sum([len(i) for i in chunks]) + sum(spaces) < maxWidth:
                diff = maxWidth - (sum([len(i) for i in chunks]) + sum(spaces))
                if len(spaces) == 0:
                    spaces.append(diff)
                else:
                    done = False
                    N = len(spaces)
                    while diff > 0:
                        for i in range(N):
                            spaces[i] += 1
                            diff -= 1
                            if diff == 0:
                                done = True
                                break
                        if done:
                            break
            if len(chunks) == 1:
                if len(spaces) == 1:
                    line = chunks[0] + ' '*spaces[0]
                else:
                    line = chunks[0]
            else:
                line = chunks[0]
                for x, y in zip(chunks[1:], spaces):
                    line += ' '*y + x
            return line

        chunks, spaces = list(), list()
        res = list()
        for word in words:
            #print(f'\tword, chunks, spaces, res = {word}, {chunks}, {spaces}, {res}')
            if len(chunks) == 0:
                chunks.append(word)
            elif sum([len(i) for i in chunks]) + len(word) + sum(spaces) + 1 <= maxWidth:
                chunks.append(word)
                spaces.append(1)
            else:
                line = processLine(chunks, spaces)
                res.append(line)
                chunks, spaces = list(), list()
                chunks.append(word)
        #print(f'word, chunks, spaces, res = {word}, {chunks}, {spaces}, {res}')
        line = ' '.join(chunks)
        line += ' ' * (maxWidth - len(line))
        res.append(line)
        return res

# Main section
for words, maxWidth in [
                          (['This', 'is', 'an', 'example', 'of', 'text', 'justification.'], 16),
                          (['What','must','be','acknowledgment','shall','be'], 16),
                          (['Science','is','what','we','understand','well','enough','to','explain','to','a','computer.','Art','is','everything','else','we','do'], 20),
                          (['This', 'is', 'an', 'example', 'of', 'text', 'justification.','a'], 16),
                          (['Science','is','what','we','understand','well','enough','to','explain','to','a','computer.','Art','is','everything','else','we','do'], 30),
                          (['Science','is','what','we','understand','well','enough','to','explain','to','a','computer.','Art','is','everything','else','we','do'], 50),
                          (['Science','is','what','we','understand','well','enough','to','explain','to','a','computer.','Art','is','everything','else','we','do'], 100),
                          (['Science','is','what','we','understand','well','enough','to','explain','to','a','computer.','Art','is','everything','else','we','do'], 10),
                          (['Science','is','what','we','understand','well','enough','to','explain','to','a','computer.','Art','is','everything','else','we','do'], 15),
                          (['abcd'], 10),
                          (['a'], 1),
                          (['a','b','c'], 5),
                          (['aa','bb','c'], 5),
                       ]:
    print(f'words, maxWidth = {words}, {maxWidth}')
    sol = Solution()
    r = sol.fullJustify(words, maxWidth)
    print(f'r = {r}')
    print('=======================')











