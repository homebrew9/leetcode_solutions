class Solution:
    #def bestClosingTime(self, customers: str) -> int:
    #    if len(set(customers)) == 1 and 'Y' in set(customers):
    #        return len(customers)
    #    min_penalty = float('inf') 
    #    curr_penalty = 0
    #    ind = len(customers)
    #    for i in range(len(customers)-1, -1, -1):
    #        if customers[i] == 'Y':
    #            curr_penalty += 1
    #        if curr_penalty <= min_penalty:
    #            min_penalty = curr_penalty
    #            if i < ind:
    #                ind = i
    #        print(f'\ti, ch, curr, min = {i}, {customers[i]}, {curr_penalty}, {min_penalty}')
    #    return ind

    def bestClosingTime(self, customers: str) -> int:
        ycount = customers.count('Y')
        ncount = 0
        penalty = 0
        ind = float('inf')
        min_penalty = float('inf')
        for i in range(0, len(customers)):
            penalty = ncount + ycount
            #print(i, ncount, ycount, penalty, min_penalty)
            if penalty < min_penalty:
                min_penalty = penalty
                ind = i
            if customers[i] == 'Y':
                ycount -= 1
            else:
                ncount += 1
            #print(f'\tind = {ind}')
        i += 1
        penalty = ncount + ycount
        #print(i, ncount, ycount, penalty, min_penalty)
        if penalty < min_penalty:
            min_penalty = penalty
            ind = i
        return ind

# Main section
for customers in [
                    'YYYY',
                    'YYNY',
                    'NNNNN',
                    'YNYYN',
                    'YYYYN',
                    'NYYYY',
                    'NYNYY',
                    'NNNYNNN',
                    'YYYNYY',
                    'NNNYYYNYYYY',
                    'YYYYYYYYYYYYYYY',
                    'YNYY',
                    'NNNNNNNNY',
                    'YNNNNNNNN',
                    'YNNNNNNNY',
                    'YNNNYNNNY',
                 ]:
    print(f'customers = {customers}')
    sol = Solution()
    r = sol.bestClosingTime(customers)
    print(f'r = {r}')
    print('======================')

