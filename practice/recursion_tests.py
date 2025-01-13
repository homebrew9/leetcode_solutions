
def reverseString(s):
    def rev(s, res):
        print(f'\ts, res = {s}, {res}')
        if s == '':
            return res
        return rev(s[1:], s[0]+res)
    return rev(s, '')



reverseString('abc')




def reverseList(arr):
    def rev(arr, res):
        print(f'\tarr, res = {arr}, {res}')
        if len(arr) == 0:
            return res
        return rev(arr[1:], [arr[0]] + res)
    return rev(arr, [])


reverseList(['a','b','c','d'])




def reverseListInplace(s):
    def rev(s, ch):
        print(f'\tarr, ch = {s}, {ch}')
        if len(s) == 0:
            return s + [ch] 
        return rev(s[1:], s[0]) + [ch]
    return rev(s[1:], s[0])


reverseListInplace(['a','b','c','d'])


reverseListInplace(['h','e','l','l','o'])


def reverseListInplace(s):
    def rev(s, ch):
        print(f'\tarr, ch = {s}, {ch}')
        if len(s) == 0:
            s = s + [ch]
            return s
        s = rev(s[1:], s[0]) + [ch]
    rev(s[1:], s[0])


s = ['a','b','c','d']

reverseListInplace(s)

print(s)




reverseListInplace(['h','e','l','l','o'])




    def reverseListInplace(s):
        def rev(s, left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            rev(s, left+1, right-1)
        rev(s, 0, len(s) - 1)


s = ['a','b','c','d']

reverseListInplace(s)

print(s)


s = ['h','e','l','l','o']

reverseListInplace(s)

print(s)




slideThrough(lst, ch) => lst

slideThrough([[]], 1)          => [[1]]
slideThrough([[1]], 2)         => [[2,1], [1,2]]
slideThrough([[2,1],[1,2]], 3) => [[3,2,1],[2,3,1],[2,1,3],[3,1,2],[1,3,2],[1,2,3]]


permute([1,2,3])
= slideThrough(permute([1,2]), 3)

permute([1,2])
= slideThrough(permute([1]), 2)

permute([1])
= slideThrough(permute([]), 1)

permute([])
= [[]]



def permute(nums):
    def slideThrough(lst, num):
        arr = list()
        for item in lst:
            for i in range(len(item)+1):
                arr.append(item[:i] + [num] + item[i:])
        return arr
    def permuteRec(nums):
        if len(nums) == 0:
            return [[]]
        return slideThrough(permuteRec(nums[:-1]), nums[-1])
    return permuteRec(nums)



permute([1])

permute([1,2])

permute([1,2,3])

permute([1,2,3,4])

permute([1,2,3,4,5])

permute([1,2,3,4,5,6])




def permute(nums):
    def slideThrough(lst, num):
        #print(f'\tlst, num = {lst}, {num}')
        arr = list()
        for item in lst:
            for i in range(len(item)+1):
                #print(f'\t\ttmp = {item[:i] + [num] + item[i:]}')
                arr.append(item[:i] + [num] + item[i:])
        return arr
    def permuteRec(nums):
        if len(nums) == 0:
            return [[]]
        return slideThrough(permute(nums[1:]), nums[0])
    return permuteRec(nums)



permute([1])

permute([1,2])

permute([1,2,3])

permute([1,2,3,4])

permute([1,2,3,4,5])

permute([1,2,3,4,5,6])

    






