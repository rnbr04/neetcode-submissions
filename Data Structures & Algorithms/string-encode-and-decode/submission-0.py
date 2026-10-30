class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for string in strs:
            metadata = f"{len(string)}#"
            encode += metadata + string
        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        pointer = 0
        len_s = len(s)

        while pointer < len_s:
            len_word = int(s[pointer])
            pointer += 2
            start = pointer
            end = start + len_word
            decode.append(s[start : end])
            pointer += len_word

        return decode 

