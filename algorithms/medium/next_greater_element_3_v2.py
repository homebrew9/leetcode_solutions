class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Narayan Pandit's algorithm - from Knuth TAOCP 4A
        if n < 10:
            return -1
        N = len(str(n))
        arr = [0 for _ in range(N)]
        i = N - 1
        while n > 0:
            p, q = divmod(n, 10)
            arr[i] = q
            i -= 1
            n = p
        print(f'\tarr = {arr}')
        found = False
        for i in range(N-2, -1, -1):
            if arr[i] < arr[i+1]:
                found = True
                break
            prev = arr[i]
        print(f'\tfound, i = {found}, {i}')
        # If we've reached the leftmost position, then
        # n is the greatest number with the digits it has.
        if i == 0 and not found:
            return -1
        # Now traverse to the right to find the next lowest digit
        found = False
        x = arr[i]
        for j in range(i+1, N):
            if arr[j] <= x:
                found = True
                break
        print(f'\tfound, j = {found}, {j}')
        # Swap digits at arr[i] and arr[j-1]/arr[j]
        if not found:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[i], arr[j-1] = arr[j-1], arr[i]
        print(f'\tarr = {arr}')
        # Now reverse the digits from i+1 till the end
        left, right = i+1, N-1
        while left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        print(f'\tarr = {arr}')
        # Now build the integer from the array
        res = 0
        for n in arr:
            res = res * 10 + n
        MAX = 2**31 - 1
        return -1 if res > MAX else res

# Main section
for n in [
            12443322,
            5432,
            5666,
            5342,
            12,
            21,
            12345,
            5106,
            5160,
            5601,
            5610,
            4321,
            432,
            164765321,
            234157641,
            164765321,
            2147483486,
            2147483645,
            2147483647,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.nextGreaterElement(n)
    print(f'r = {r}')
    print('================')



