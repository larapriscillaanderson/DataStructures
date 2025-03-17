# Level 1 String Concatenation:

# Note: using the + operator to concatenate strings in Python will not automatically add a space
# Have to add space on your own

string1 = "Hello"
string2 = "World"
result = string1 + " " + string2
print(result)
# Output: Hello World

# Level 2 String Concatenation:

# Note: using the * operator will repeat a string a specific number of times

string = "abc"
result = string * 3
print(result)
# Output: abcabcabc

# Level 3 String Concatenation:

# Note: using the .join() built in function in Python will not automatically add a space
# Helpful to use when concatenating multiple strings, especially if they are in a list form

strings = ["Python", "is", "fun"]
result = " ".join(strings)
print(result)
# Output: Python is fun

# Level 4 String Concatenation:

# Note: using f-strings (formatted string literals) can be used to embed expressions 
# inside string literals
# Have to add spacing within the string literal

name = "Aquamarine"
age = 29
result = f"My name is {name} and I am {age} years old."
print(result)
# Output: My name is Aquamarine and I am 29 years old.

# Level 5 String Concatenation:

# Note: using the += operator does not automatically add a space
# Useful for when you need to extend an existing string by appending another string to it

message = "Python "
message += "Rocks!"
print(message)
# Output: Python Rocks!

# Level 6 String Concatenation:

# Note: using str.format() does not automatically add a space
# helpful in replacing placeholders with values

string1 = "Hello"
string2 = "World"
result = "{} {}".format(string1, string2)
print(result)
# Output: Hello World
