import base64
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        res = 'https://tinyurl.com/'
        longUrl_enc = base64.b64encode(longUrl.encode('utf-8'))
        longUrl_enc_str = longUrl_enc.decode('utf-8')
        res += longUrl_enc_str
        print(f'\tres = {res}')
        return res

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        url_enc_str = shortUrl.replace('https://tinyurl.com/', '')
        url_enc_b = url_enc_str.encode('utf-8')
        originalUrl = base64.b64decode(url_enc_b).decode('utf-8')
        #print(url_enc_b)
        #print(originalUrl)
        return originalUrl

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

