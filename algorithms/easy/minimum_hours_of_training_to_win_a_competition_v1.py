from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        hours = 0
        for engy, expr in zip(energy, experience):
            if initialEnergy > engy:
                initialEnergy -= engy
            else:
                hours += engy + 1 - initialEnergy
                initialEnergy = 1
            if initialExperience > expr:
                initialExperience += expr
            else:
                hours += expr + 1 - initialExperience
                initialExperience = 2 * expr + 1
        return hours

# Main section
for initialEnergy,      \
    initialExperience,  \
    energy,             \
    experience in [
                     (5, 3, [1,4,3,2], [2,6,3,1]),
                     (2, 4, [1], [3]),
                     (30, 78, [24,91,63,38,31,63,22,35,91,54,88,46,80,14,12,19,57,92], [18,43,36,88,84,21,82,54,61,80,68,54,75,27,99,14,86,95])
                  ]:
    print(f'initialEnergy, initialExperience = {initialEnergy}, {initialExperience}')
    print(f'energy     = {energy}')
    print(f'experience = {experience}')
    sol = Solution()
    r = sol.minNumberOfHours(initialEnergy, initialExperience, energy, experience)
    print(f'r = {r}')
    print('=======================')

