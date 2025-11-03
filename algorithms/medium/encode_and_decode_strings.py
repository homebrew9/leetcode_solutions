from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return chr(0).join(list(map(lambda x: '|'.join([str(ord(ch)) for ch in list(x)]), strs)))

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return list(map(lambda x: ''.join([chr(int(i)) if i != '' else '' for i in x.split('|')]), s.split(chr(0))))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# Main section
#  ["Hello","World"]
#  [""]























