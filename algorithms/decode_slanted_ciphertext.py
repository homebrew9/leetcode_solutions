class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        retval = ''
        matrix = list()
        cols = len(encodedText)//rows
        matrix.append([])
        r = 0
        c = 0
        for ch in encodedText:
            #print(ch)
            matrix[r].append(ch)
            c += 1
            if c == cols:
                c = 0
                r += 1
                if r < rows:
                    matrix.append([])
        print(f'{matrix}')
        # Now read the matrix
        #print('~~~~~~~~~~~~~~~~~~')
        bln_endofstring = False
        r = 0
        #col_end = len(''.join(matrix[0]).rstrip())
        #print(f'{col_end}')
        for c in range(cols):
            #if matrix[r][c] == ' ':
            #    break
            #print(f'{matrix[r][c]}')
            print(f'(r, c) = ({r}, {c})')
            retval += matrix[r][c]
            iter = c + 1
            if iter == cols:
                break
            for r1 in range(1, rows):
                print(f'  >>> (r1, iter) = ({r1}, {iter})')
                #print(f'{matrix[r1][iter]}')
                if iter == cols - 1 and matrix[r1][iter] == ' ':
                    bln_endofstring = True
                    break
                retval += matrix[r1][iter]
                iter += 1
                if iter == cols:
                    break
            if bln_endofstring:
                break
        return retval.rstrip()
        
# Main section
sol = Solution()
for encodedText, rows in [
                              #('ch   ie   pr', 3),
                              #('iveo    eed   l te   olc', 4),
                              #('coding', 1),
                              #('tsodab   h vani   eaerdg    rlk     wey      o        ol       d', 8),
                              #(' b  ac', 2),
                              #('   a', 2),
                              ('       abcd ', 2),
                         ]:
    print(f'encodedText, rows = [{encodedText}], [{rows}]')
    r = sol.decodeCiphertext(encodedText, rows)
    print(f'r = [{r}]')
    print('=====================================')


