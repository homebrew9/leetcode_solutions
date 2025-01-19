#
# This is an example of Cycle Sort, which uses the minimum number of swaps to sort an array.
# Check Wikipedia article on cycle sort.
#

def min_swap_count(arr):
    sorted_arr = sorted(arr)
    pos = {v: i for i, v in enumerate(sorted_arr)}
    print(f'\tpos = {pos}')
    swaps = 0
    for i in range(len(arr)):
        print(f'\t\ti, arr[i] = {i}, {arr[i]}')
        while (j := pos[arr[i]]) != i:
            print(f'\t\t\tSwap (i, arr[i]) <-> (j, arr[j]) ; ({i}, {arr[i]}) <-> ({j}, {arr[j]})')
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    print(f'\tFinal arr = {arr}')
    return swaps

# Main section
for arr in [
              [16,9,3,17,19,15,5],
           ]:
    print(f'arr = {arr}')
    r = min_swap_count(arr)
    print(f'r = {r}')
    print('=======================')


