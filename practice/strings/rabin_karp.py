# ==================================================================================================
# Rabin Karp algorithm - given two strings "needle" and "haystack", return the index in "haystack"
# of the first occurrence of "needle". If "needle" does not exist in "haystack" return -1.
# The rolling hash fails for some cases - it's not clear why.
# ==================================================================================================

import random
def search(needle, haystack):
    def getHash(s):
        # This is my own bare-bones Hash function
        res = 0
        for ch in s:
            res = res*10 + ord(ch)
        return res
    def rollingHash(hsh, size, ch1, ch2):
        return (hsh - ord(ch1)*(10**(size-1)))*10 + ord(ch2)
    if len(needle) > len(haystack):
        return -1
    hsh_needle = getHash(needle)
    N = len(needle)
    for i, v in enumerate(haystack[:-N+1]):
        if i == 0:
            chunk = haystack[:N]
            #print(f'\ti, chunk = {i}, {chunk}')
            hsh_chunk = getHash(chunk)
            if hsh_chunk == hsh_needle:
                if haystack[:N] == needle:
                    return 0
        else:
            #print(f'\ti, chunk, pre, post = {i}, {haystack[i:i+N]}, {haystack[i-1]}, {haystack[i+N-1]}')
            hsh_chunk = rollingHash(hsh_chunk, N, haystack[i-1], haystack[i+N-1])
            if hsh_chunk == hsh_needle:
                if haystack[i:i+N] == needle:
                    return i
    return -1

def searchRabinKarp(needle, haystack):
    def calculateHash(s):
        base = 256
        mod = 101
        res = 0
        for ch in s:
            res = (res * base + ord(ch)) % mod
        return res
    def calculateRollingHash(hsh, c1, c2):
        # This Hash function is from: https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
        # hash('a')   =      ord('a') % 101
        # hash('ab')  =    ((ord('a') * 256) % 101 + ord('b')) % 101
        # hash('abr') =  ( ((ord('a') * 256) % 101 + ord('b')) % 101 ) * 256 + ord('r')) % 101
        base = 256
        mod = 101
        salt = (base % mod) * base
        hsh1 = ((hsh + mod - ord(c1) * salt % mod) * base + ord(c2)) % mod
        return hsh1
    if len(needle) > len(haystack):
        return -1
    hsh_needle = calculateHash(needle)
    N = len(needle)
    for i, v in enumerate(haystack[:-N+1]):
        if i == 0:
            chunk = haystack[:N]
            #print(f'\ti, chunk = {i}, {chunk}')
            hsh_chunk = calculateHash(chunk)
            #print(f'\t\thsh_chunk, hash(chunk), hsh_needle = {hsh_chunk}, {calculateHash(haystack[i:i+N])}, {hsh_needle}')
            if hsh_chunk == hsh_needle:
                if haystack[:N] == needle:
                    return 0
        else:
            #print(f'\ti, chunk, pre, post = {i}, {haystack[i:i+N]}, {haystack[i-1]}, {haystack[i+N-1]}')
            hsh_chunk = calculateRollingHash(hsh_chunk, haystack[i-1], haystack[i+N-1])
            #print(f'\t\thsh_chunk, hash(chunk), hsh_needle = {hsh_chunk}, {calculateHash(haystack[i:i+N])}, {hsh_needle}')
            if hsh_chunk == hsh_needle:
                if haystack[i:i+N] == needle:
                    return i
    return -1

# Main section
for needle, haystack in [
                           ('abc', 'xyzpqrmnodefabcjkl'),
                           #('aaabc', 'aaaaaaaaaaaaaaaaaaabbbbbbccccccaaaaaaaaaabccccccc'),
                           #('thequick', 'the'),
                           ('where', 'thequestionsarewhatwhyhowwhenwhere'),
                        ]:
    print(f'needle, haystack = {needle}, {haystack}')
    r1 = search(needle, haystack)
    r2 = searchRabinKarp(needle, haystack)
    print(f'r1, r2, cmp = {r1}, {r2}, {r1 == r2}')
    print('================')

#  # Random testing
#  for _ in range(10):
#      needle = ''.join([chr(random.randint(97,122)) for _ in range(3)])
#      haystack = ''.join([chr(random.randint(97,122)) for _ in range(100000)])
#      r1 = search(needle, haystack)
#      r2 = searchRabinKarp(needle, haystack)
#      print(f'r1, r2, cmp = {r1}, {r2}, {r1 == r2}')
#      print('================')


