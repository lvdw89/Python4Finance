#!/usr/bin/python
import re

# https://docs.python.org/3/howto/regex.html

# remove special meaning of meta character [ using  blackslash.
line = '['
matchObj = re.match('\[', line)
print(matchObj.group())

# match any digit.
line = '1a£'
matchObj = re.match('\d', line)
print(matchObj.group())

line = 'abcbd'
target = 'a[bcd]*b'
matchObj = re.match(target, line)
print(matchObj.group())

# backslash plague
line = '\section'
target = '\\\\section'
matchObj = re.match(target, line)
print(matchObj.group())

# backslash plague -> Im expecting \n to be printed, not sure why this doesnt work.
line = '\n'
target = r'\n'
matchObj = re.match(target, line)
print(matchObj.group())

p = re.compile('[a-z]+')
m = p.match('tempo')
print(m.start())

# start with module level functions..
