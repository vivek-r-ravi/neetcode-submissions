# brute force: convert each char to ord and have two separators
class Solution:
    def encode(self, strs: List[str]) -> str:
        self.split_char = "#"
        self.split_str = " "
        self.empty_str = "EMPTY"
        encoded = []
        for s in strs:
            if s == "":
                encoded.append(self.empty_str)
            else:
                encoded.append(self.split_char.join([str(ord(c)) for c in s]))
        return self.split_str.join(encoded)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        str_list = s.split(self.split_str)
        out = []
        for string in str_list:
            if string == self.empty_str:
                out.append("")
            else:
                out.append("".join([chr(int(c)) for c in string.split(self.split_char)]))
        return out
