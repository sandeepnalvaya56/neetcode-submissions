import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        n = len(s)
        #take care of the edge case
        if n <= 1:
            return True
        #Start algorithm
        s = s.lower()
        print(s)
        for i in range(n):
            ri = n-i-1
            if s[i] == s[ri]:
                if ri == 0:
                    return True
                else:
                    continue
            else:
                return False
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left=0
        right=len(s)-1
        if right <= 0:
            return True
        while left<right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

