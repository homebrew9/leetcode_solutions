# ================================================================
# Bubble sort: Iterate through the array and keep swapping adjacent
# elements if they are out of order. Stop when no more swaps done.
# ================================================================
def bubbleSort(nums):
    N = len(nums)
    for j in range(N-1, -1, -1):
        for i in range(0, j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

def bubbleSort_1(nums):
    has_swapped = True
    # If no swap has occurred, the list is sorted
    while has_swapped:
        has_swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                has_swapped = True
    return nums

# Main section
for nums in [
               [7,3,2,5,6,10,9,8,1],
               [91,-95,74,-72,-33,20,31,33,-65,93,-17,98,8,88,-16,68,-92,36,-23,-89],
               [867,-446,-835,-587,0,514,892,-254,73,-31,914,-318,-467,-19,-844,-600,152,-974,368,-887,143,728,443,-559,-835,-928,846,555,-160,725,795,-313,956,763,529,-586,-138,864,564,704,228,-2,-567,-619,834,957,-197,-99,754,410],
               [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
               [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1],
            ]:
    print(f'nums = {nums}')
    r1 = bubbleSort(nums)
    print(f'r1   = {r1}')
    r2 = bubbleSort_1(nums)
    print(f'r2   = {r2}')
    print('Testing assertion...')
    assert(r1 == r2 == sorted(nums))
    print('===========================')

