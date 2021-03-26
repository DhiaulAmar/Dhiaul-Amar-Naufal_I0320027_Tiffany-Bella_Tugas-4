#   EXERCISE 4.1
print("Exercise 4.1")
x = 15
y = 4

#Output : x + y = 19
print('x + y =', x+y)

#output : x - y = 11
print('x - y =', x-y)

#output : x * y = 60
print('x * y =', x*y)

#output : x / y = 3.75
print('x / y =',x/y)

#output : x // y = 3
print('x // y =', x//y)

#output : x ** y = 50625
print('x ** y =', x**y)


#   EXERCISE 4.2
print("\n", "Exercise 4.2")
x = 15
x = 10
y = 12

#output : x > y is False
print('x > y is', x>y)

#output : x < y is True
print('x < y is', x<y)

#output : x == y is False
print('x == y is', x==y)

#output x != y is True
print('x != y is', x!=y)

#output : x >= y False
print('x >= is', x>=y)

#output : x <= y is True
print('x <= y is', x<=y)


#   EXERCISE 4.3
print("\n", "Exercise 4.3")
x = True
y = False

print('x and y is', x and y)

print('x or y is', x or y)

print('not x is', not x)


#   EXERCISE 4.4
print("\n", "Exercise 4.4")
# Strings
str1 = "Hello"
str2 = "World"

# concat
result = str1 + " " + str2

# output
print(result);


#   exercise 4.5
print("\n", "Exercise 4.5")
# string
str = "HA"

#replicate
result = str * 3

#output
print(result)


#   EXERCISE 4.6
print("\n", "Exercise 4.6")
# srings
needle = "lo"
haystack = "Hello Wolrd"

# check
if needle in haystack:
    print(needle, "is present in string", haystack)

else:
    print("Not found")


#   EXERCISE 4.7
print("\n", "Exercise 4.7")
# strings
needle = "HA"
haystack = "Hello World"

#check
if needle in haystack:
    print(needle, "is present in the sring", haystack)

else:
    print("Not found")


#   EXERCISE 4.8
print("\n", "Exercise 4.8")
# string
str = "Jane Doe"

# character
ch = str[1]

# output
print(ch)      #a

#   EXERCISE 4.9
print("\n", "Exercise 4.9")
# string
str = "Hello World"

# substring
substr = str[3:5]

# output
print(substr)       # lo


#   EXERCISE 4.10
print("\n", "exercise 4.10")
string =      "Hello World"
skipping :     "x x x x x"       # charcters marked wit x
final_str = "HloWrd"

# string
str = "Hello World"

# skip
new_str = str[0::2]
print(new_str)


#   EXERCISE 4.11
print("\n", "Exercise 4.11")
# string
str = "Hello World"

# reverse
result = str[::-1]

# output
print(result)
