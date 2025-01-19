class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        hsh = defaultdict(list)
        hsh1 = defaultdict(list)
        arr = [0 for _ in range(10)]
        for n in nums:
            key = int(str(n)[0])
            if len(set(str(n))) == 1:
                arr[key] += len(str(n))
            elif str(n) == str(key) + '0'*(len(str(n))-1):
                hsh1[key] += [str(n)]
            else:
                hsh[key] += [str(n)]
        print(arr)
        print(hsh)
        print(hsh1)
        res = ''
        for i in range(9,-1,-1):
            if arr[i] > 0:
                #print('in if')
                lst = hsh[i] + [str(i) * arr[i] + str(i) * 10]
                #print(f'lst = {lst}')
                res += ''.join(sorted(lst, reverse=True)).replace(str(i)*10, '',1)
            elif i in hsh:
                res += ''.join(sorted(hsh[i], reverse=True))
            res += ''.join(sorted(hsh1[i]))
        return res
                
