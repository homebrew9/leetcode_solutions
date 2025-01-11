#
# Does not work!
#
from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        energy_needed = sum(energy)
        max_experience = max(experience)
        ind = experience.index(max_experience)
        sum_upto_max_experience = sum(experience[:ind])
        print(f'\tenergy_needed = {energy_needed}')
        print(f'\tmax_experience = {max_experience}')
        print(f'\tind = {ind}')
        print(f'\tsum_upto_max_experience = {sum_upto_max_experience}')
        
        if initialEnergy > energy_needed and initialExperience + sum_upto_max_experience > max_experience:
            return 0
        
        hours_for_energy = energy_needed - initialEnergy + 1
        hours_for_experience = (max_experience - sum_upto_max_experience + 1) - initialExperience
        print(f'\thours_for_energy = {hours_for_energy}')
        print(f'\thours_for_experience = {hours_for_experience}')
        
        return (hours_for_energy + hours_for_experience)

# Main section
for initialEnergy,      \
    initialExperience,  \
    energy,             \
    experience in [
                     (30, 78, [24,91,63,38,31,63,22,35,91,54,88,46,80,14,12,19,57,92], [18,43,36,88,84,21,82,54,61,80,68,54,75,27,99,14,86,95])
                  ]:
    print(f'initialEnergy, initialExperience = {initialEnergy}, {initialExperience}')
    print(f'energy     = {energy}')
    print(f'experience = {experience}')
    sol = Solution()
    r = sol.minNumberOfHours(initialEnergy, initialExperience, energy, experience)
    print(f'r = {r}')
    print('=======================')

