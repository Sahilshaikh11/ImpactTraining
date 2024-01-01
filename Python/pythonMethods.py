"""
============================================================================================================================================

# SPLIT Method
a = input().split("2")
print(a)
print(type(a))

============================================================================================================================================

# Evaluate Method
a = eval(input())
print(a)

============================================================================================================================================

# Typecasting of lists element
a = [int(i) for i in input().split()]
print(type(a[1]))

============================================================================================================================================

# Keywords in Python
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

============================================================================================================================================

# Slicing [start_index : stop_index : step_count]
s = "Happy Coding & avoid 69"
print(s[1:20:1])
print(s[::-1]) # Reversed Str will print

============================================================================================================================================

# Pallindrome
s = str(input())
print("yes" if s == s[::-1] else "no")

============================================================================================================================================

# Ternary Operations
a, b=25, 35
print(("NO","YES") [a+b<100]) # Method 1
print((<False condition>, <True Condition> [<Condition>])) # Method 2
print({True:"YES",False:"NO"} [100<200]) # Method 2 Ex.

============================================================================================================================================

# Membership Operators(in, not in)
print("a" in "shahil")

============================================================================================================================================

# End method
a=int(input())
for i in range(1,11):
    print(f"{i}*{a}=",i*a, end=" ")

============================================================================================================================================

# len(), max() and min() - here max and min will return the element based on the ascii values
a=input().split("1")
print(a)
print(len(max(a)))

============================================================================================================================================

# create hollow box of hashes
n=int(input())
for i in range(n):
    if (i==0 or i==n-1):
        print(n*"# ")
    else:
        print("# "+"  "*(n-2)+" #")

===================================================================================================================================================

# format() (To format the output
# Area of the circle

pi=3.14
r=12.5
area = pi*r**2

print("Area :",area)
import math
area1 = math.pi*r**2
print("Area1 :{:.2f}".format(area1))  # that means the value in the variable (area1) will be stored in the :.2f telling that we want to print only 2 values after the decimal point.
print("Area of the circle with radius {} is : {:.4f}".format(r,area1))  # Here the r will be stored in the {} and the (area1) will be stored in the :.4f
print(math.pi)
                   
a,b=100,200
print("sum of {} + {} = {}".format(a,b,(a+b)))

====================================================================================================================================================

# Built in string methods:
a="hello python... happy new year"
print(a.capitalize()) # Capitalize 0th index character of the string
print(a.title()) # Capitalize every first char of words present in string

===============================================================================================================================================

# center(width, fillchar) --> returns string with length width, padded with filllchar
a="Python"
print(a.center(12,'*')) # Keeps the string in center of the length width and fill the rest with fillchar
print(a.ljust(12,"#")) # Keeps the string in left of the length width and fill the rest with fillchar
print(a.rjust(12,'-')) # Keeps the string in right of the length width and fill the rest with fillchar
print(a.zfill(12)) 

==============================================================================================================================================

# Count(sub, start, end) --> returns count of sub string from start to end position
a="This is Python, Py is VHLL"
print(a.count("is"))
print(a.count("is",2))
print(a.count("is",2,10))

===============================================================================================================================================

# endsWith(suffix, [start], [end]) --> checks if the string ends with the given suffix
a= "Hello Python"
print(a.endswith("on"))

===============================================================================================================================================

# find(str, start, end) --> returns the index of the str if present else -1
a="Hello Python"
print(a.find('th'))

================================================================================================================================================
# isalpha() --> checks if the strings is alphabets or not
a="HappyNewYear"
print(a.isalpha())

# isdigit() --> checks if the string is digit or not
a="354684654"
print(a.isdigit())

# isalmun() --> checks for either alpha or digit or both
a="Happy190283109"
print(a.isalnum())

# isspace() --> checks for white space 
a="        "
print(a.isspace()) 

# swapcase() --> swaps the cases of aphabets
a="Happy New Year"
print(a.swapcase())

# join() --> Concatenates the string with given str
a = ['p','y','t','h','o','n']
print("".join(a))
print("*".join(a))

# strip() --> removes the extra spaces from the string
a="   This is Python   "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

=====================================================================================================================

# enumerate() 
s="sowbarnika"
for i,ch in enumerate(s):
    print(ch, "-->", i)

=====================================================================================================================

# Creation of empty list
parul = []
parul = list()
print(parul, type(parul))
parul= [12, 56.2, True, [10, 20, 30], 'Hello']
print(parul[3][1])
----------------------------------------------------
a=[1, 2, 3]
print(a+[4, 5, 6])
print(a.append([ 4, 5, 6]))
print(a.extend([4, 5, 6]))
print(a.insert(25, 100)) # at index 25 element 100 will be added, if index outof bound element will be inserted at last
priny(a.pop()) # will remove last element of the list

=====================================================================================================================
"""
