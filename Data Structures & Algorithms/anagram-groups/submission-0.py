from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # in valid anagram compare two dictionaries -> return result
        # create a word count dictionary of current word from the list of words
        # here we have to compare current dictionary against a group of dictionaries, so we create a dictionary of dictionaries
        # Word is the key, and a dictionary of the string's word count is the value
        # Our data structure needs to have the word stored in a tuple to be the key, so we can add multiple keys for the same dictionary value
        # It would look like multi_key_dict = {
        # ('key1_a', 'key1_b'): dict1{},
        # ('key2_a', 'key2_b', 'key2_c'): dict2{}
        #    }
        # For the current dictionary matching, we will iterate through the key & value of the dictionary using enumerate ".items" method
        # We will check if current dictionary matches the value(dictionary)
        # If Found:
        #   Append the string to the existing key tuple for which the dictionary value has matched
        # If Found:
        #   Create a new key tuple and add the current dictionary as the value

        seen = {}
        for string in strs:
            current_dict = {}
            for char in string:
                if char in current_dict:
                    current_dict[char] += 1
                else:
                    current_dict[char] = 1
            
            if current_dict in seen.values(): # if the current dict is already present
                for key, value in seen.items():
                    if value == current_dict:
                        new_key = key + (string,)
                        new_value = current_dict # to avoid confusion, it is same as value
                        seen.pop(key)
                        seen[new_key] = new_value
                        break
            else:
                key = (string,)
                value = current_dict
                seen[key] = value
        
        final_list = []
        for item in seen.keys():
            final_list.append(list(item))
        
        return final_list



            
            
                    





        