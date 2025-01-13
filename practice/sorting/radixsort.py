#
# RadixSort - sort a given list of integers
#
def sortList(nums):
    def radixSort(nums, pos, lim):
        #print(f'\tpos, lim, nums = {pos}, {lim}, {nums}')
        if len(nums) == 0 or pos >= lim:
            return [int(n) for n in nums]
        hsh = {i: [] for i in range(10)}
        arr = list()
        prev, curr = None, None
        for n in nums:
            curr = n[:pos]
            k = int(n[pos])
            #print(f'\tn, prev, curr, k, hsh = {n}, {prev}, {curr}, {k}, {hsh}')
            if prev is None or curr == prev:
                hsh[k] += [n]
            else:
                for key in range(10):
                    if len(hsh[key]) > 0:
                        for val in hsh[key]:
                            arr.append(val)
                hsh = {i: [] for i in range(10)}
                hsh[k] += [n]
            prev = curr
        for k in range(10):
            if len(hsh[k]) > 0:
                for v in hsh[k]:
                    arr.append(v)
        return radixSort(arr, pos+1, lim)
    lim = 8 
    lst1 = [str(abs(n)).zfill(lim) for n in nums if n < 0]
    lst2 = [str(n).zfill(lim) for n in nums if n >= 0]
    lst = [-i for i in radixSort(lst1, 0, lim)[::-1]] + radixSort(lst2, 0, lim)
    return lst

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
    r = sortList(nums)
    print(f'r    = {r}')
    print('================')

