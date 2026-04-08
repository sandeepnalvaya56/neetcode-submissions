class Solution:

    def encode(self, strs: List[str]) -> str:
        # Write your code here
        result = ""
        for string in strs:
            result = result + str(len(string)) + "#" + string
        return result

    def decode(self, s: str) -> List[str]:
        # Write your code here
        result = []
        i=0
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            final_string = s[j+1 : j+1+length]
            result.append(final_string)
            i = j+1+length
        return result

