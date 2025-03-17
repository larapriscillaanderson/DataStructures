# Level 1 .join(iterable):

# Note: .join() takes each item from iterable and inserts the separator between them

words = ["Hello", "World"]
result = " ".join(words)
print(result)
# Output: Hello World

# Level 2 .join(iterable):

# Note: .join() can be used to insert anything within a string between each element

print("-".join(["Hello", "World"]))
# Output: Hello-World
print("🚀".join(["Python", "is", "fun"]))  
# Output: Python🚀is🚀fun

# Level 3 .join(iterable):

# Note: .join() can have an edge case where there is only one element

print(" ".join(["Hello"]))
# Output: Hello 
# No spaces were added in this case, since there's nothing to join, 
# the separator isn't needed

# Level 4: .join(iterable):

# Note: .join() can be used with an empty string as a separator

print("".join(["H", "e", "l", "l", "o"]))
# Output: Hello
# This case has concatenated everything without any spacing.

# Level 5: .join(iterable):

# Note: .join() can be used to insert a separator between individual characters within a string

text = "Hello"
result = "*".join(text)
print(result)
# Output: H*e*l*l*o
# Notice how the iterable is just one single string, versus the other examples had the string
# within square brackets for a list
