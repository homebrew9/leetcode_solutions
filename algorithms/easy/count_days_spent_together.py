#
# Logic is sound, but does not work for the last test case!!
#
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def commonDays(start, end):
            days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            commonDays = 0
            # start is always <= end
            start_month, start_day = [int(i) for i in start.split('-')]
            end_month, end_day = [int(i) for i in end.split('-')]
            if start_month == end_month:
                commonDays = end_day - start_day + 1
            else:
                for i in range(start_month+1, end_month):
                    commonDays += days[i]
                commonDays += (days[start_month] - start_day) + (end_day) + 1
            return commonDays
            
        alice_arrive = [int(i) for i in arriveAlice.split('-')]
        alice_leave = [int(i) for i in leaveAlice.split('-')]
        bob_arrive = [int(i) for i in arriveBob.split('-')]
        bob_leave = [int(i) for i in leaveBob.split('-')]
        
        daysTogether = 0
        if (alice_arrive[0] == bob_arrive[0] == alice_leave[0] and alice_arrive[1] <= bob_arrive[1] <= alice_leave[1]) or \
           (alice_arrive[0] <= bob_arrive[0] <= alice_leave[0]):
            # Bob arrives while Alice is already there
            daysTogether = commonDays(arriveBob, min(leaveBob, leaveAlice))
        elif (bob_arrive[0] == alice_arrive[0] == bob_leave[0] and bob_arrive[1] <= alice_arrive[1] <= bob_leave[1]) or \
             (bob_arrive[0] <= alice_arrive[0] <= bob_leave[0]):
            # Alice arrives while Bob is already there
            daysTogether = commonDays(arriveAlice, min(leaveAlice, leaveBob))
        
        return daysTogether

# Main section
for arriveAlice, leaveAlice, arriveBob, leaveBob in [
       #('08-15', '08-18', '08-16', '08-19'),
       #('10-01', '10-31', '11-01', '12-31'),
       #('01-20', '11-30', '02-01', '12-01'),
       #('02-01', '02-02', '02-02', '02-03'),
       #('06-01', '06-15', '06-16', '06-30'),
       #('01-01', '12-31', '01-01', '12-31'),
       #('05-10', '05-11', '05-10', '05-11'),
       #('06-12', '06-12', '06-12', '06-12'),
       #('02-10', '02-15', '08-13', '08-20'),
       #('08-13', '08-20', '02-10', '02-15'),
       ('04-20', '06-18', '04-12', '12-19'),
    ]: 
    print(f'arriveAlice, leaveAlice, arriveBob, leaveBob = {arriveAlice}, {leaveAlice}, {arriveBob}, {leaveBob}')
    sol = Solution()
    r = sol.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
    print(f'r = {r}')
    print('=========================')

