from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # Intuition: It's easier to determine the count of subarrays that have *at least* k consonants.
        # We find at_least_k() for k consonants and (k-1) consonants and return the diff.
        def at_least_k(k):
            hsh_vowel = defaultdict(int)
            consonant_count = 0
            res = 0
            i = 0
            for j in range(N):
                if word[j] in 'aeiou':
                    hsh_vowel[word[j]] += 1
                else:
                    consonant_count += 1
                while len(hsh_vowel) == 5 and consonant_count >= k:
                    res += N - j
                    if word[i] in 'aeiou':
                        hsh_vowel[word[i]] -= 1
                        if hsh_vowel[word[i]] == 0:
                            del hsh_vowel[word[i]]
                    else:
                        consonant_count -= 1
                    i += 1
            return res
        N = len(word)
        return at_least_k(k) - at_least_k(k+1)

# Main section
for s, k in [
               ('aeioqq', 1),
               ('aeiou', 0),
               ('ieaouqqieaouqq', 1),
               ('aeiouqaeiou', 1),
               ('aeiouqaeiouq', 2),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.countOfSubstrings(s, k)
    print(f'r = {r}')
    print('====================')

