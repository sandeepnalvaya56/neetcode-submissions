from collections import Counter
class Solution:
    result = []
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        keys = {}
        for text in strs:
            keyList = [0]*26
            #freqMap = Counter(text)
            # anagram is a dictionary 
            # Can the dictionary be a key?
            # Or can we represent anagrams in some other way?
            # Trick is to use a hashset - each letter has its unique position in english alphabet - 26 characters, so 26 positions in a hashset
            # Each position (index) represents the character and its value represents the frequency of that character
            # To identify the position of the character, we need ord() function
            for letter in text:
                index = ord(letter) - ord("a")
                keyList[index] += 1
            key = tuple(keyList)
            if key in keys:
                keys[key].append(text)
            else:
                keys[key] = [text]
        return [keys[key] for key in keys]

