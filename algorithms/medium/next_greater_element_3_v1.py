class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Narayan Pandit's algorithm - from Knuth TAOCP 4A
        if n < 10:
            return -1
        arr = list(str(n))
        size = len(arr)
        i = size - 1
        while i >= 1 and arr[i] <= arr[i - 1]:
            i -= 1
        if i == 0:
            return -1
        x = i - 1
        j = x
        while j + 1 < size and arr[j + 1] > arr[x]:
            j += 1
        y = j
        # Swap elements at positions x and y
        arr[x], arr[y] = arr[y], arr[x]
        # Now reverse the array slice arr[x+1:]
        arr = arr[:x+1] + arr[x+1:][::-1]
        # Very important note:
        # "if there is a valid answer but it does not fit in 32-bit integer, return -1."
        res = int(''.join(arr))
        if res > 2**31 - 1:
            return -1
        return int(''.join(arr))

# Main section
for n in [
            #12,
            #21,
            #12345,
            #5106,
            #5160,
            #5601,
            #5610,
            #4321,
            #432,
            #164765321,
            #234157641,
            #164765321,
            2147483486,
            2147483645,
            2147483647,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.nextGreaterElement(n)
    print(f'r = {r}')
    print('================')


