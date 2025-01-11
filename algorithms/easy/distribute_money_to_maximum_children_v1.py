class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # See if we can distribute the money evenly
        if children * 8 == money:
            return children
        
        # Every child must get at least 1 dollar
        if money < children:
            return -1

        # Hand over 1 dollar to each child first and decrement the money
        money -= children
        
        # If every child now has $7 more (i.e. $8 in total) and their total
        # amount is less than money, then one child gets more than $8. The
        # remaining (children - 1) have exactly $8. E.g. money = 100, children = 3
        if children * 7 < money:
            return children - 1
        
        # How many additional $7 can we give to each child? From divmod operation
        # below: money = p * 7 + q
        # p children will have $7 more (so those p children will have $8 total)
        # 1 child will have $q more
        # Examples:
        # a) m, c =  8, 3 => after $1 dist. m =  5, c = 3 => p, q = divmod(5 , 7) = 0, 5
        # b) m, c = 10, 3 => after $1 dist. m =  7, c = 3 => p, q = divmod(7 , 7) = 1, 0
        # c) m, c = 13, 3 => after $1 dist. m = 10, c = 3 => p, q = divmod(10, 7) = 1, 3
        # d) m, c = 20, 3 => after $1 dist. m = 17, c = 3 => p, q = divmod(17, 7) = 2, 3
        p, q = divmod(money, 7)

        # If p is zero, no one gets $8 exactly; everyone gets less than $8 - Case a) above
        # ($q can be divided amongst the children in any combination).
        if p == 0:
            return 0

        # One corner case we have to check for is q = 3, and also how many children p have $7
        # Case d) above - after $1 distribution, we have this for children array: [1, 1, 1]
        # After divmod operation, we have: [8, 8, 4] => here we cannot modify $4 distribution,
        # we will have to remove some money from the second $8 i.e. [8, 7, 5] or similar. Hence,
        # we return p - 1
        if q == 3 and p == children - 1:
            return p - 1

        # However, for Case c) above - after $1 distribution, we have this for children array:
        # [1, 1, 1]. After divmod operation, we have [8, 4, 1] => here we don't have to touch $8
        # distribution; we can remove money from $4 and move to $1 => [8, 3, 2]. Hence we return p.
        # The difference between Case c) and Case d) is:
        # Case c) => [8, 8, 8, ... 8, 4]            i.e. (N - 1) $8 and exactly one $4 distribution
        # Case d) => [8, 8, 8, ... 8, 4, 1, ..., 1] i.e. (N - k) $8, one $4 distribution, and (k - 1) $1 distributions
        # For Case b) also, we return p because there were no $4 distributions at all.
        # Case b) - after $1 distribution, we have: [1, 1, 1]. After divmod operation, we have [8, 1, 1]
        return p

# Main section
for money, children in [
                          (8, 3),
                          (2, 2),
                          (2, 1),
                          (100, 3),
                          (100, 12),
                          (100, 13),
                          (100, 14),
                          (100, 15),
                       ]:
    print(f'money, children = {money}, {children}')
    sol = Solution()
    r = sol.distMoney(money, children)
    print(f'r = {r}')
    print('===================')

