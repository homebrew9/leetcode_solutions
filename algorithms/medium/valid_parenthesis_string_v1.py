from collections import defaultdict

class Solution:
    def checkValidString(self, s: str) -> bool:
        def solve(i, t):
            #print(f'{">"*(i)} solve({i}, {t})')
            if i >= len(s):
                return t == 0
            if t < 0:
                return False
            if (i, t) in self.hsh:
                return self.hsh[(i, t)]
            tmp = None
            if s[i] == '(':
                tmp = solve(i + 1, t + 1)
            elif s[i] == ')':
                tmp = solve(i + 1, t - 1)
            else:
                for delta in (1, -1, 0):
                    tmp1 = solve(i + 1, t + delta)
                    tmp = tmp1 if tmp is None else tmp or tmp1
            self.hsh[(i, t)] = tmp
            return self.hsh[(i, t)]
        self.hsh = defaultdict(int)
        res = solve(0, 0)
        return res

# Main section
for s in [
            '()',
            '(*)',
            '(*))',
            '**((',
            '*****(((((',
            '()*(*((()(()(*)*))*)',
            '*)((*)(())(()(*)(**)',
            '((*))(**)*((()(*))()*)))*)*((*))*(())**(*))()**()(',
            '((()(*(()((*)())(*(*)*((()**())***)))))()))*((*))(',
            '()((()()))*((*)*))*()*)((***(****)()(*)***)((*(**)()**)()(**))(*))*(((*)*((**()()(()*())**)))()(*()*',
            '))()(*()()(((((*)(*((*()(*()*()*)*******)()***()))*)()(***))(**(*)()()(()((()*())))()*()(()*(*)()*()',
            '**(*((()*))()**)*()((**(()****((())()*)()*(*(*)**(***)*))*))****(((()*(**(()((******)((*((())(((((*(',
            ')***()(()***)()*)*)(*())(*)(*))()(((()*(*)(()))(**)))*)*)(*()(**)((*(*()(()()())(()()()*(*)(((*(****',
            '*)*((*)))(*)*()***(****(**(*(*))*(*****))*)**((*))*(*(((()*((((())*()(**()****((((**(()))(*()**((**)',
            '*()))*)()(*)**))****(((**(()*))(***))***(((*)*))**)*)(***)*(*(*)(**)*)))**(*(()))(*))()**)(((*)))((*',
            ')**(*)*)**)(*)(*)()(**))()()*(**))((*)()**)))*)(**)*)())**(())*(((**))*((((*())(**)((*())*))))((*)*)',
            '****************************************************************************************************',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.checkValidString(s)
    print(f'r = {r}')
    print('=================')

