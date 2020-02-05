string = "Welcome to Python!"

# Select all ascii letter from string
s = []
for c in string:
    if c.isalnum(): s.append(c)
print('for loop', s, '\n')
print('list comprehensions:', [c for c in string if c.isalpha()], '\n')
print('filter function call:', list(filter(lambda c: c.isalpha(), string)), '\n')

print('\n\n')
# Convert all chars to upper case
s = []
for c in string:
    s.append(c.upper())

print('for loop:', s, '\n')
print('list comprehentions:', [c.upper() for c in string], '\n')
print('map function call:', list(map(lambda c: c.upper(), string)), '\n')

print('\n\n')
# Combine 2 above action together
s = []
for c in string:
    if c.isalpha(): s.append(c.upper())

print('for loop:', s, '\n')
print('list comprehensions:', [c.upper() for c in string if c.isalpha()], '\n')
print('map & filter call:', list(map(lambda c: c.upper(), filter(lambda c: c.isalpha(), string))))
