# ================================================================
# Heap Sort: Heapsort is an optimization of Selection Sort. We
# can use the max heap data structure to keep track of the max
# element and keep sending it to the rightmost position. In this
# program, we have actually implemented the "heapify" procedure!
# We could've used Python's max-heap implementation as well.
# ================================================================

def heap_sort(lst):
    def max_heapify(heap_size, index):
        left, right = 2 * index + 1, 2 * index + 2
        largest = index
        if left < heap_size and lst[left] > lst[largest]:
            largest = left
        if right < heap_size and lst[right] > lst[largest]:
            largest = right
        if largest != index:
            lst[index], lst[largest] = lst[largest], lst[index]
            max_heapify(heap_size, largest)

    # heapify original lst
    for i in range(len(lst) // 2 - 1, -1, -1):
        max_heapify(len(lst), i)

    # Use heap to sort elements
    for i in range(len(lst)-1, 0, -1):
        # Swap last element with first element
        # We know that the first element of the max-heap is the greatest. By sending
        # it to the end, we have sent it to its rightful place. We will then ignore
        # the last index and heapify the rest of the array. Again the max element will
        # arrive at the first position. We then repeat this process.
        lst[i], lst[0] = lst[0], lst[i]
        # We reduce the heap size by 1 in each iteration
        max_heapify(i, 0)
    return lst

# Main section
for nums in [
               [7,3,2,5,6,10,9,8,1],
               [7,3,2,9,10,5,0,8,1],
               [91,-95,74,-72,-33,20,31,33,-65,93,-17,98,8,88,-16,68,-92,36,-23,-89],
               [867,-446,-835,-587,0,514,892,-254,73,-31,914,-318,-467,-19,-844,-600,152,-974,368,-887,143,728,443,-559,-835,-928,846,555,-160,725,795,-313,956,763,529,-586,-138,864,564,704,228,-2,-567,-619,834,957,-197,-99,754,410],
               [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
               [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1],
            ]:
    print(f'nums = {nums}')
    r = heap_sort(nums)
    print(f'r    = {r}')
    print('Testing assertion...')
    assert(r == sorted(nums))
    print('===========================')

