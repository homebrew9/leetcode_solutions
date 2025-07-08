from typing import List
import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = list()
        for cd, biz, act in zip(code, businessLine, isActive):
            is_code_valid = len(cd) > 0 and re.match(r'^[a-zA-Z0-9_]+$', cd)
            is_biz_valid = biz in ('electronics', 'grocery', 'pharmacy', 'restaurant')
            is_act_valid = act is True
            if is_code_valid and is_biz_valid and is_act_valid:
                res.append((cd, biz))
        return [c for c, b in sorted(res, key=lambda x: (x[1], x[0]))]

# Main section
for code, businessLine, isActive in [
                                       (['SAVE20','','PHARMA5','SAVE@20'], ['restaurant','grocery','pharmacy','restaurant'], [True,True,True,True]),
                                       (['GROCERY15','ELECTRONICS_50','DISCOUNT10'], ['grocery','electronics','invalid'], [False,True,True]),
                                    ]:
    print(f'code         = {code}')
    print(f'businessLine = {businessLine}')
    print(f'isActive     = {isActive}')
    sol = Solution()
    r = sol.validateCoupons(code, businessLine, isActive)
    print(f'r            = {r}')
    print('===================')

