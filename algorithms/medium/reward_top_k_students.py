from typing import List

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        st_pos = set(positive_feedback)
        st_neg = set(negative_feedback)
        print(f'\tst_pos = {st_pos}')
        print(f'\tst_neg = {st_neg}')
        hsh = dict()
        for i, r in zip(student_id, report):
            score = 0
            for w in r.split():
                if w in st_pos:
                    score += 3
                elif w in st_neg:
                    score -= 1
            print(f'\t\ti, score = {i}, {score}')
            hsh[i] = score
        print(f'\thsh = {hsh}')
        arr = [i for i, j in sorted(hsh.items(), key=lambda x: (-x[1], x[0]))]
        return arr[:k]

# Main section
for positive_feedback, negative_feedback, report, student_id, k in [
                (['smart','brilliant','studious'], ['not'], ['this student is studious','the student is smart'], [1,2], 2),
                (['smart','brilliant','studious'], ['not'], ['this student is not studious','the student is smart'], [1,2], 2),
             ]:
    print(f'positive_feedback, negative_feedback, report, student_id, k = {positive_feedback}, {negative_feedback}, {report}, {student_id}, {k}')
    sol = Solution()
    r = sol.topStudents(positive_feedback, negative_feedback, report, student_id, k)
    print(f'r = {r}')
    print('================')
           
