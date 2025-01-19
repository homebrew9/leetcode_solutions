#
# Solution for next permutation using Narayan Pandita's algorithm is good.
# But the solution for counting swaps is incorrect. See last test case: num = '059', k = 5.
# The permutation is '950' and '059 -> '950' = 3 swaps. But this algorithm returns 1 because
# it counts non-adjacent swaps! Just use brute force and selection sort.
#
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def sign(x):
            if x < 0:
                return -1
            if x > 0:
                return 1
            return 0
        def minAdjSwaps(s1, s2):
            N = len(s1)
            arr1 = [int(x) for x in s1]
            arr2 = [int(x) for x in s2]
            arr = [0] * N
            for i in range(0, N):
                found = False
                for j in range(i+1, N):
                    if arr2[j] == arr1[i]:
                        arr[i] = j - i
                        arr2[j] = -1 
                        found = True
                        break
                if not found:
                    for j in range(i-1, -1, -1):
                        if arr2[j] == arr1[i]:
                            arr[i] = j - i
                            arr2[j] = -1
                            break
            print(f'\tarr = {arr}')
            swaps = 0
            stack = list()
            for n in arr:
                #if n == 0:
                #    continue
                done = False
                while stack and sign(stack[-1]) != sign(n):
                    tmp = stack.pop()
                    swaps += 1
                    val = tmp + n
                    if val == 0:
                        done = True
                        break
                    n = val
                if done:
                    continue
                stack.append(n)
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
                 #('1234123', 1),
                 #('1234123', 2),
                 #('1234123', 3),
                 #('1234123', 4),
                 #('1234123', 5),
                 #('1234123', 6),
                 #('1234123', 7),
                 #('1234123', 8),
                 #('1234123', 9),
                 #('1234123', 10),
                 #('5489355142', 4),
                 #('11112', 4),
                 #('00123', 1),
                 ('059', 5),
              ]:
    print(f'num, k = {num}, {k}')
    sol = Solution()
    r = sol.getMinSwaps(num, k)
    print(f'r      = {r}')
    print('=====================')


