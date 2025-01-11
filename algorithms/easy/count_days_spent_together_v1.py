class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def daysFromStart(dt):
            days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            mth, day = [int(i) for i in dt.split('-')]
            total = 0
            for i in range(1, mth):
                total += days[i]
            total += day
            return total

        alice_start = daysFromStart(arriveAlice)
        alice_end = daysFromStart(leaveAlice)
        bob_start = daysFromStart(arriveBob)
        bob_end = daysFromStart(leaveBob)

        days_together = 0
        if alice_start == bob_start and alice_end == bob_end:
            days_together = alice_end - alice_start + 1
        elif alice_start <= bob_start <= alice_end:
            days_together = min(alice_end, bob_end) - bob_start + 1
        elif bob_start <= alice_start <= bob_end:
            days_together = min(alice_end, bob_end) - alice_start + 1
        
        return days_together

# Main section
for arriveAlice, leaveAlice, arriveBob, leaveBob in [
       ('08-15', '08-18', '08-16', '08-19'),
       ('10-01', '10-31', '11-01', '12-31'),
       ('01-20', '11-30', '02-01', '12-01'),
       ('02-01', '02-02', '02-02', '02-03'),
       ('06-01', '06-15', '06-16', '06-30'),
       ('01-01', '12-31', '01-01', '12-31'),
       ('05-10', '05-11', '05-10', '05-11'),
       ('06-12', '06-12', '06-12', '06-12'),
       ('02-10', '02-15', '08-13', '08-20'),
       ('08-13', '08-20', '02-10', '02-15'),
       ('04-20', '06-18', '04-12', '12-19'),
    ]: 
    print(f'arriveAlice, leaveAlice, arriveBob, leaveBob = {arriveAlice}, {leaveAlice}, {arriveBob}, {leaveBob}')
    sol = Solution()
    r = sol.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
    print(f'r = {r}')
    print('=========================')


