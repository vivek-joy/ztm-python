print(type("hi hello there 24"))
username = 'supercoder'
password = 'supersecret'

long_string = '''
This is
a
long string
'''
# string concatenation
print(username + " " + password)

# will not work
# print("hello" + 5)

weather = "It\'s always \"sunny\" in philadelphia"
print(weather)

# formatted strings
name="Johny"
age = 20
print(f'hi {name}. You are  {age} years old')

# string indexes
print(name[1:5])
print(name[::2])
print(name[-2])
print(name[::-1])