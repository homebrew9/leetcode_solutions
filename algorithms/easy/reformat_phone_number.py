class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')
        arr = list()
        i = 0
        while i < len(number):
            if i + 4 >= len(number):
                #print(number[i:])
                #arr.append(number[i:])
                if len(number[i:]) > 3:
                    arr.append(number[i:i+2])
                    arr.append(number[i+2:])
                else:
                    arr.append(number[i:])
                break
            else:
                #print(number[i:i+3])
                arr.append(number[i:i+3])
                i += 3
        return '-'.join(arr)
# Main section
for number in [
                 '12',
                 '123',
                 '1234',
                 '12345',
                 '123456',
                 '1234567',
                 '12345678',
                 '123456789',
                 '1234567890',
                 '12345678901',
                 '123456789012',
                 '1234567890123',
                 '12345678901234',
              ]:
    print(f'number = {number}')
    sol = Solution()
    r = sol.reformatNumber(number)
    print(f'r = {r}')
    print('================')

