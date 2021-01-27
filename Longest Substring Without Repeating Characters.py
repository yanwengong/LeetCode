### Longest Substring Without Repeating Characters
### 20210126
### two pointers

## Given a string s, find the length of the longest substring without repeating characters.


## Yang script


## my script
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        unique_char = set(s)
        if len(unique_char) == 1:
            return 1

        def _update_list(char_list, char):
            new_char_list=[]
            for i in range(len(char_list)):
                if char_list[i] == char:
                    for j in range(i+1,len(char_list)):
                        new_char_list.append(char_list[j])
                    return new_char_list


        str_len = len(s)
        char_list = [] # char_set = set()
        counter = []
        j = 0
        c = 0
        counter.append(0)
        for i in range(str_len):
            if s[i] not in char_list:
                char_list.append(s[i])
                counter[c] += 1
            else:
                j += 1
                char_list = _update_list(char_list, s[i])
                char_list.append(s[i])
                counter.append(len(char_list))
                c += 1



        return max(counter)
