class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        # iterate through the array
        for string in strs:
            # add string_length metadata before the actual string
            metadata = f"{len(string)}#"

            encode += metadata + string
        return encode

    def decode(self, s: str) -> List[str]:
        # array to hold the result
        decode = []
        # pointer to iterate through the array
        left_pointer = 0
        # length of encoded string
        len_s = len(s)

        while left_pointer < len_s:
            # iterate through the string to find the first "#" symbol
            right_pointer = left_pointer
            while s[right_pointer] != "#":
                right_pointer += 1
            
            # the length of string is from left -> right pointer 
            # just before the "#" symbol
            len_str = int(s[left_pointer : right_pointer])
            # append the string to array
            decode.append(s[right_pointer+1 : right_pointer + len_str + 1])
            # shift left_pointer to next word
            left_pointer = right_pointer + len_str + 1

        return decode

