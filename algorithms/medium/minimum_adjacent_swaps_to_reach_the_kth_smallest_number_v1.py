#
# Solution for next permutation using Narayan Pandita's algorithm is good.
# To count number of adjacent swaps, we use brute force with a variation of Selection Sort.
# Selection Sort has the lowest number of swaps amongst sorting algorithms.
#
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def minAdjSwaps(s1, s2):
            N = len(s1)
            arr1 = [int(x) for x in s1]
            arr2 = [int(x) for x in s2]
            swaps = 0
            for i in range(0, N):
                if arr2[i] == arr1[i]:
                    continue
                for j in range(i+1, N):
                    if arr1[j] == arr2[i]:
                        ind = j
                        break
                for k in range(ind, i, -1):
                    # Swap the current and previous element in arr1
                    arr1[k], arr1[k-1] = arr1[k-1], arr1[k]
                    swaps += 1
                if arr1 == arr2:
                    return swaps
            return swaps
        def next_permutation(num):
            # Narayan Pandita's algorithm for the next permutation
            arr = list(num)
            # Find greatest j for which A[j] < A[j+1]
            for ind in range(N-1):
                if arr[ind] < arr[ind+1]:
                    j = ind
            # Find greatest i, where i > j, for which A[i] > A[j]
            for ind in range(j+1, N):
                if arr[ind] > arr[j]:
                    i = ind
            # Now swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
            # Sort the chunk A[j+1:N]
            arr = arr[:j+1] + sorted(arr[j+1:])
            return ''.join(arr)
        N = len(num)
        orig = num
        for _ in range(k):
            num = next_permutation(num)
        print(f'permut = {num}')
        ind = 0
        for i in range(N):
            if orig[i] != num[i]:
                ind = i
                break
        res = minAdjSwaps(orig[ind:], num[ind:])
        return res


# Main section
for num, k in [
                 ('5489355142', 4),
                 ('11112', 4),
                 ('00123', 1),
                 ('059', 5),
                 ('1234123', 1),
                 ('1234123', 2),
                 ('1234123', 3),
                 ('1234123', 4),
                 ('1234123', 5),
                 ('1234123', 6),
                 ('1234123', 7),
                 ('1234123', 8),
                 ('1234123', 9),
                 ('1234123', 10),
              ]:
    print(f'num, k = {num}, {k}')
    sol = Solution()
    r = sol.getMinSwaps(num, k)
    print(f'r      = {r}')
    print('=====================')


