# Level 1 Slicing:

# s[start:stop:step]
# s[::-1]

# Level 2 Slicing:

s = "hello"
reversed_s = s[::-1]
print(reversed_s)  
# Output: "olleh"

# Level 3 Slicing:

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # split the string into words
        words = s.split()
        
        # reverse each word using slicing
        reversed_words = [word[::-1] for word in words]  # ✅ Fixed syntax
        
        # join the reversed words back with spaces
        result = ' '.join(reversed_words)
        
        # return the new sentence but reversed in result
        return result
