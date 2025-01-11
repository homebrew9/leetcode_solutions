from itertools import zip_longest

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hsh = dict()
        bull_count, cow_count = 0, 0
        for i, j in zip_longest(secret, guess):
            if i == j:
                bull_count += 1
            else:
                if i is not None:
                    if i in hsh:
                        hsh[i][0] += 1
                        if hsh[i][0] > 0 and hsh[i][1] > 0:
                            cow_count += 1
                            hsh[i][0] -= 1
                            hsh[i][1] -= 1
                    else:
                        hsh[i] = [1,0]
                if j is not None:
                    if j in hsh:
                        hsh[j][1] += 1
                        if hsh[j][0] > 0 and hsh[j][1] > 0:
                            cow_count += 1
                            hsh[j][0] -= 1
                            hsh[j][1] -= 1
                    else:
                        hsh[j] = [0,1]
        return f'{bull_count}A{cow_count}B'

# Main section
for secret, guess in [
                        ('1807', '7810'),
                        ('1123', '0111'),
                        ('1123090', '0903201'),
                        ('0903201', '1123090'),
                     ]:
    print(f'secret, guess = {secret}, {guess}')
    sol = Solution()
    r = sol.getHint(secret, guess)
    print(f'r = {r}')
    print('==================')

