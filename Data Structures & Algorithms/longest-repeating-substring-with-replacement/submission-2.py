from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount = 0
        l=0 # left index
        char_length = Counter()
        
        for r in range(len(s)):
            char_length[s[r]] +=1
            maxCount = max(maxCount, char_length[s[r]])
            is_valid = (r - l + 1) - maxCount <= k
            
            if not is_valid:
                char_length[s[l]] -= 1
                l += 1
            
            max_length = r - l + 1
        return max_length



            




