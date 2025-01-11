class Solution:
    def distinctIntegers(self, n: int) -> int:
        st = set()
        st.add(n)
        for _ in range(1000):
            arr = list()
            for x in st:
                for i in range(1, n+1):
                    if x % i == 1:
                        arr.append(i)
            for elem in arr:
                st.add(elem)
        print(st)
        return len(st)

# Main section
for n in [
            1,
            2,
            3,
            4,
            5,
            10,
            20,
            29,
            43,
            50,
            67,
            71,
            97,
            100,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.distinctIntegers(n)
    print(f'r = {r}')
    print('===============')

