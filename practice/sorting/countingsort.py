# ===================================================================================
# Check the Wikipedia link for the pseudocode of the Counting Sort algorithm
# https://en.wikipedia.org/wiki/Counting_sort
# ===================================================================================

def sortListCS(nums):
    def countingSort(nums,low,high):
        arr = [0 for _ in range(high - low + 1)]
        for n in nums:
            arr[n - low] += 1
        lst = list()
        for i, v in enumerate(arr):
            for _ in range(v):
                lst.append(i + low)
        return lst
    return countingSort(nums, min(nums), max(nums))


def sortListCSWiki(nums):
    def countingSort(nums, k):
        N = len(nums)
        count = [0 for _ in range(k+2)]
        output = [None for _ in range(N)]
        # Create histogram in "count" array
        for i in range(N):
            j = nums[i]
            count[j] += 1
        # Compute prefix sum in "count" array
        for i in range(1, k+1):
            count[i] += count[i-1]
        # Populate "output" array using "input" and "count" arrays
        for i in range(N-1, -1, -1):
            j = nums[i]
            count[j] -= 1
            output[count[j]] = j
        return output
    return countingSort(nums, max(nums))


def sortListMS(nums):
    def mergeSort(nums):
        if len(nums) == 1:
            return nums
        N = len(nums)
        arr1 = mergeSort(nums[:N//2])
        arr2 = mergeSort(nums[N//2:])
        return merge(arr1, arr2)
    def merge(arr1, arr2):
        arr = list()
        N, M = len(arr1), len(arr2)
        i, j = 0, 0
        while i < N and j < M:
            if arr1[i] == arr2[j]:
                arr.append(arr1[i])
                arr.append(arr2[j])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1
        while i < N:
            arr.append(arr1[i])
            i += 1
        while j < M:
            arr.append(arr2[j])
            j += 1
        return arr
    return mergeSort(nums)


for nums in [
               [24,27,94,-42,100,-46,-38,47,46,35,48,36,37,22,50,-54,-76,27,82,-81,25,44,-39,-35,1,76,-41,100,-67,-12,-99,83,-68,-90,-10,-44,24,-93,11,-80,90,41,27,43,-29,-1,-51,-40,-36,81],
               [-9,-72,-70,-47,-23,-44,-27,2,92,-79],
               [-7,-3,2,1,-5,9,0,5,6,-2,-8,8,0,-2,-10,4,-9,3,-5,-5],
               [13,-1,8,15,10,-1,-8,-2,-13,1,-2,-9,8,-1,-1,-11,1,0,8,10],
               [10,-1,13,12,0,-2,4,1,1,5,3,2,1,13,6,-1,15,7,4,0],
               [10,9,8,5,2,9,10,4,1,4,3,6,9,4,6],
               [-3,-2,-1,0,0,6,7,7,8,8,8,10,10,11,11,12,12,13,14,15],
               [12,12,11,10,10,9,9,7,5,4,3,2,1,0,-1,-2,-2,-3,-3,-5],
            ]:
    print(f'nums = {nums}')
    r = sortListCS(nums)
    print(f'r    = {r}')
    assert(sorted(nums) == r)
    r = sortListMS(nums)
    print(f'r    = {r}')
    assert(sorted(nums) == r)
    print('=====================================')


for nums in [
               [24, 27, 94, 42, 100, 46, 38, 47, 46, 35, 48, 36, 37, 22, 50, 54, 76, 27, 82, 81, 25, 44, 39, 35, 1, 76, 41, 100, 67, 12, 99, 83, 68, 90, 10, 44, 24, 93, 11, 80, 90, 41, 27, 43, 29, 1, 51, 40, 36, 81],
               [9, 72, 70, 47, 23, 44, 27, 2, 92, 79],
               [7, 3, 2, 1, 5, 9, 0, 5, 6, 2, 8, 8, 0, 2, 10, 4, 9, 3, 5, 5],
               [13, 1, 8, 15, 10, 1, 8, 2, 13, 1, 2, 9, 8, 1, 1, 11, 1, 0, 8, 10],
               [10, 1, 13, 12, 0, 2, 4, 1, 1, 5, 3, 2, 1, 13, 6, 1, 15, 7, 4, 0],
               [10, 9, 8, 5, 2, 9, 10, 4, 1, 4, 3, 6, 9, 4, 6],
               [3, 2, 1, 0, 0, 6, 7, 7, 8, 8, 8, 10, 10, 11, 11, 12, 12, 13, 14, 15],
               [12, 12, 11, 10, 10, 9, 9, 7, 5, 4, 3, 2, 1, 0, 1, 2, 2, 3, 3, 5],
            ]:
    print(f'nums = {nums}')
    r = sortListCSWiki(nums)
    print(f'r    = {r}')
    assert(sorted(nums) == r)
    print('=====================================')


