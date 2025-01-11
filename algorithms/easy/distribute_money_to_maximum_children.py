#
# Does not work!
#
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        if money < 8 and children >= 2:
            return 0
        arr = [0 for _ in range(children)]
        N = len(arr)
        for i in range(N):
            if i == N - 1:
                arr[i] = money
            else:
                if money >= 8:
                    arr[i] = 8
                    money -= 8
                else:
                    arr[i] = money
                    money = 0
            if money == 0:
                break
        print(money, arr)
        cnt_4 = sum([n == 4 for n in arr])
        cnt_0 = sum([n == 0 for n in arr])
        if cnt_4 == 0 and cnt_0 == 0:
            return arr.count(8)
        elif cnt_4 == 1 and cnt_0 == 0:
            return arr.count(8) - 1
        elif cnt_0 == 1 and cnt_4 == 0:
            return arr.count(8) - 1
        else:
            cnt = cnt_4 + cnt_0 - 4
            p, q = divmod(cnt, 7)
            if q == 0:
                tmp = arr.count(8) - p
            else:
                tmp = arr.count(8) - p - 1
            if tmp < 0:
                return -1
            else:
                return tmp
        return -1

# Main section
for money, children in [
                          (8, 3),
                          (2, 2),
                          (2, 1),
                       ]:
    print(f'money, children = {money}, {children}')
    sol = Solution()
    r = sol.distMoney(money, children)
    print(f'r = {r}')
    print('===================')

