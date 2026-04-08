class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        if not s or not t:
            return ""
        tMap = Counter(t) 
        sMap = {}
        have = 0
        need = len(tMap)
        l=0
        minLength = float('inf')
        for r in range(len(s)):
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]:
                have += 1
            
            while have == need:
                if r-l+1 < minLength:
                    result = s[l:r+1]
                    minLength = r-l+1 
                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l = l+1
                
        return result
