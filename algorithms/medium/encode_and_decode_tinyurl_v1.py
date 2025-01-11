import random
import string

class Codec:

    def __init__(self):
        self.hsh = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # Generate a "base" string whose length is a prime number.
        # Then pick a "center" at random and use the left 4 characters and right 4 characters
        # to form a key. The hash key is used to store the longUrl. The idea is that the key
        # would be random enough to avoid collisions.
        res = 'https://tinyurl.com/'
        base = ''.join([random.choices(string.ascii_lowercase+string.ascii_uppercase+string.digits)[0] for _ in range(263)])
        N = len(base)
        center = random.randint(4, N-4)
        key = base[center-4:center+4]
        self.hsh[key] = longUrl
        res += key
        print(f'\tres = {res}')
        return res

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.replace('https://tinyurl.com/', '')
        return self.hsh[key]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

for url in [
              'https://leetcode.com/problems/design-tinyurl',
              'http://badge.example.net/beginner.aspx?aftermath=achiever&actor=air',
           ]:
    print(f'url = {url}')
    codec = Codec()
    r = codec.decode(codec.encode(url))
    print(f'r   = {r}')
    assert(url == r)
    print('====================')


