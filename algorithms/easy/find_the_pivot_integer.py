#
# Binary Search did not work during the contest!!
# Trying it out in v1 script.
#
class Solution:
    #def pivotInteger(self, n: int) -> int:
    #    if n == 1:
    #        return n
    #    total = n * (n+1) // 2
    #    low, high = 1, n
    #    print(f'\tlow, high = {low}, {high}')
    #    while low < high:
    #        mid = (low + high) // 2
    #        left_sum = mid * (mid+1) // 2
    #        right_sum = total - left_sum
    #        if left_sum == right_sum:
    #            return mid
    #        elif left_sum < right_sum:
    #            low = mid + 1
    #        else:
    #            right = mid - 1
    #        print(f'\t\tlow, mid, high = {low}, {mid}, {high}')
    #    print(f'\tlow, mid, high = {low}, {mid}, {high}')
    #    return -1

    #def pivotInteger(self, n: int) -> int:
    #    if n == 1:
    #        return n
    #    total = n * (n+1) // 2
    #    i = 1
    #    while True:
    #        left_sum = i * (i+1) // 2
    #        right_sum = total - left_sum + i
    #        #print(f'\ti, left_sum, right_sum = {i}, {left_sum}, {right_sum}')
    #        if left_sum == right_sum:
    #            return i
    #        elif left_sum < right_sum:
    #            i += 1
    #        else:
    #            break
    #    return -1

    def pivotInteger(self, n: int) -> int:
        # Left sum need not be "i*(i+1)//2"; we can just have
        # running total.
        if n == 1:
            return n
        total = n * (n+1) // 2
        i = 1
        left_sum = 0
        while True:
            left_sum += i
            right_sum = total - left_sum + i
            #print(f'\ti, left_sum, right_sum = {i}, {left_sum}, {right_sum}')
            if left_sum == right_sum:
                return i
            elif left_sum < right_sum:
                i += 1
            else:
                break
        return -1

# Main section
for n in [
            8,
            1,
            4,
            1000,
            256,
            134,
            789,
            580,
            990,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.pivotInteger(n)
    print(f'r = {r}')
    print('=======================')

