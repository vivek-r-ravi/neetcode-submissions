# brute force: convert each char to ASCII value and have two separators
# O(m) time and space
class SolutionV1:
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


# canonical solution: prefix string length + separator
# O(m) time and space
class Solution:
    def encode(self, strs: List[str]) -> str:
        self.split_char = "#"
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + "#" + s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        out = []
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            i += 1
            length = int(length)
            string = s[i : i + length]
            out.append(string)
            i += length
        return out
