class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        n = len(s)
        
        counter = 0
        seen = {}
        j = 0
        while j < n:
            if s[j] in seen:
                counter = 0
                j = seen[s[j]] + 1
                seen = {}

            else:
                counter += 1
                maxLength = max(maxLength, counter)
                seen[s[j]] = j
                j = j+1
                
            
        return maxLength

