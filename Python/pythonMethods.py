"""
======================================================================
# SPLIT Method
a = input().split("2")
print(a)
print(type(a))
======================================================================
# Evaluate Method
a = eval(input())
print(a)
======================================================================
# Typecasting of lists element
a = [int(i) for i in input().split()]
print(type(a[1]))
======================================================================
# Keywords in Python
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
======================================================================
# Slicing [start_index : stop_index : step_count]
s = "Happy Coding & avoid 69"
print(s[1:20:1])
print(s[::-1]) # Reversed Str will print
======================================================================
# Pallindrome
s = str(input())
print("yes" if s == s[::-1] else "no")
======================================================================
# Ternary Operations
a, b=25, 35
print(("NO","YES") [a+b<100]) # Method 1
print((<False condition>, <True Condition> [<Condition>])) # Method 2
print({True:"YES",False:"NO"} [100<200]) # Method 2 Ex.
======================================================================
# Membership Operators(in, not in)
print("a" in "shahil")
======================================================================
# End method
a=int(input())
for i in range(1,11):
    print(f"{i}*{a}=",i*a, end=" ")
======================================================================
# len(), max() and min() - here max and min will return the element based on the ascii values
a=input().split("1")
print(a)
print(len(max(a)))
======================================================================
# create hollow box of hashes
n=int(input())
for i in range(n):
    if (i==0 or i==n-1):
        print(n*"# ")
    else:
        print("# "+"  "*(n-2)+" #")
======================================================================
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
======================================================================
"""

