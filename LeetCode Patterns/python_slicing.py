# Level 1 Slicing:

# s[start:stop:step]
# s[::-1]

# Level 2 Slicing:

s = "hello"
reversed_s = s[::-1]
print(reversed_s)  
# Output: "olleh"

# Level 3 Slicing:

text = "Hello"
result = ""
for char in text: 
    result += char + "*"
# removes the trailing *
# [:-1] basically give me everything except the last character
result = result[:-1]
print(result)
# Output: H*e*l*l*o

# Level 4 Slicing:

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # split the string into words
        words = s.split()
        
        # reverse each word using slicing
        reversed_words = [word[::-1] for word in words]
        
        # join the reversed words back with spaces
        result = ' '.join(reversed_words)
        
        # return the new sentence but reversed in result
        return result
