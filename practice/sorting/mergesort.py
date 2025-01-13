#
# MergeSort - sort a given list of integers
#
def sortNums(nums, logic):
    def mergeSort(nums, logic):
        N = len(nums)
        if N == 1:
            return nums
        arr1 = mergeSort(nums[:N//2], logic)
        arr2 = mergeSort(nums[N//2:], logic)
        if logic == 1:
            return merge(arr1, arr2)
        elif logic == 2:
            return merge_1(arr1, arr2)

    def merge(arr1, arr2):
        arr = list()
        N, M = len(arr1), len(arr2)
        i, j = 0, 0
        while i < N or j < M:
            if i >= N:
                arr.append(arr2[j])
                j += 1
            elif j >= M:
                arr.append(arr1[i])
                i += 1
            elif arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i += 1
            elif arr2[j] < arr1[i]:
                arr.append(arr2[j])
                j += 1
            else:
                arr.append(arr1[i])
                arr.append(arr2[j])
                i += 1
                j += 1
        return arr

    def merge_1(arr1, arr2):
        arr = list()
        N, M = len(arr1), len(arr2)
        i, j = 0, 0
        while i < N and j < M:
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i += 1
            elif arr2[j] < arr1[i]:
                arr.append(arr2[j])
                j += 1
            else:
                arr.append(arr1[i])
                arr.append(arr2[j])
                i += 1
                j += 1
        while i < N:
            arr.append(arr1[i])
            i += 1
        while j < M:
            arr.append(arr2[j])
            j += 1
        return arr
    return mergeSort(nums, logic)

# Main section
for nums in [
               [5,-6,-10,3,-4,1,3,8,-7,-6],
               [12,-18,-12,14,-1],
               [-6,18,1,-8,-18,20,-13,-12,-18],
               [13,-14,-16,-63,73,66,-43,99,-47,-8,80,74,87,-90,-34,-67,100,-7,-77,41],
               [4,78,85,21,-30,76,46,82,-37,-21,-46,-21,-4,-54,-47,-31,-84,-9,8,-98,-66,60,-28,83,-12],
               [9,8,7,6,5,4,3,2,1,0],
               [8,8,8,8,8,8,8,8,8,8,8,8,8],
            ]:
    print(f'nums = {nums}')
    r1 = sortNums(nums, 1)
    print(f'r1   = {r1}')
    r2 = sortNums(nums, 2)
    print(f'r2   = {r2}')
    print('================')


