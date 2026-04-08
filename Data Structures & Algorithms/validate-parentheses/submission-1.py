class Solution:
    def isValid(self, s: str) -> bool:
        checkParentheses = {"}" : "{", ")" : "(" , "]" : "["}
        # "()[]{}"
        currListStack = []
        for char in s:
            if char in checkParentheses:
                if  not currListStack:
                    return False
                if checkParentheses[char] != currListStack[-1]:
                    return False
                else:
                    currListStack.pop()
            else:
                currListStack.append(char)
        if len(currListStack) > 0:
            return False
        else:
            return True
                
