class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def convertToMin(s):
            hour, minute = [int(i) for i in s.split(':')]
            total = 0
            for h in range(hour):
                total += 60
            total += minute
            return total
        
        curr_min = convertToMin(current)
        corr_min = convertToMin(correct)
        if curr_min == corr_min:
            return 0
        
        add_mins = [60, 15, 5, 1]
        i = 0
        res = 0
        while curr_min < corr_min:
            if curr_min + add_mins[i] <= corr_min:
                res += 1
                curr_min += add_mins[i]
            else:
                i += 1
                if curr_min + add_mins[i] <= corr_min:
                    res += 1
                    curr_min += add_mins[i]
                else:
                    i += 1
                    if curr_min + add_mins[i] <= corr_min:
                        res += 1
                        curr_min += add_mins[i]
                    else:
                        i += 1
                        if curr_min + add_mins[i] <= corr_min:
                            res += 1
                            curr_min += add_mins[i]
        return res

# Main section
for current, correct in [
                           ('02:30', '04:35'),
                           ('11:00', '11:01'),
                           ('00:00', '23:59'),
                           ('00:01', '23:58'),
                        ]: 
    print(f'current, correct = {current}, {correct}')
    sol = Solution()
    r = sol.convertTime(current, correct)
    print(f'r = {r}')
    print('=========================')

