class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        if not strs:
            return ""
        for text in strs:
            n=len(text)
            encoded = encoded+str(n)+"#"+text
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        result = []
        n = len(s)
        length = ""
        i=0
        while i <= n-1:
            if not s[i] == "#":
                length = length+s[i]
                i+=1
            else:
                result.append(s[i+1:i+1+int(length)])
                i = i+1+int(length)
                length = ""
        return result





            