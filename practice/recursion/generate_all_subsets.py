def generate_subsets(arr):
    def subsets(lst, i, n):
        if len(lst) >= n:
            res.append(lst)
            return
        if i >= N:
            return
        for j in range(i, N):
            subsets(lst + [arr[j]], j+1, n)
    N = len(arr)
    res = list()
    for size in range(1, N+1):
        for i, v in enumerate(arr):
            subsets([v], i+1, size)
    return res

def generate_subsets_v1(arr):
    # https://afteracademy.com/blog/print-all-subsets-of-a-given-set/
    def allSubsets(pos, len, subset):
        if pos == N:
            res.append(subset)
            return
        allSubsets(pos+1, len+1, subset)             # Try current element in the subset
        allSubsets(pos+1, len, subset + [arr[pos]])  # Skip the current element
    N = len(arr)
    subset = list()
    res = list()
    allSubsets(0, 0, subset)
    return res

def generate_subsets_v2(arr):
    # https://afteracademy.com/blog/print-all-subsets-of-a-given-set/
    # Clean approach using Bit-masking
    N = len(arr)
    res = list()
    for i in range(1<<N):
        curr = list()
        for j in range(N):
            if i & (1<<j) != 0:
                curr.append(arr[j])
        res.append(curr)
    return res

# Main section
for arr in [
              ['x'],
              [0,1],
              [1,2,3],
              ['a','b','c','d'],
              ['a','b','c','d','e'],
           ]:
    print(f'arr = {arr}')
    r1 = generate_subsets(arr)
    print(f'r1  = {r1}')
    r2 = generate_subsets_v1(arr)
    print(f'r2  = {r2}')
    r3 = generate_subsets_v2(arr)
    print(f'r3  = {r3}')
    print('======================')


