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

# format() To format the output
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

# sort() --> to sort a list (can Modify the list), sorted() --> to sort anything (can't modify)
li = [10,23,9,1,87,54,34]
li.sort()
print(sorted(li))
print(li)
# Reverse
print(sorted(li, reverse = True))
li.sort(reverse=True)
res = list(reversed(li)) # will not modify the original list
print(res)

=====================================================================================================================

# List Comprehension
li=[i*i for i in range(11)]
print(li)

=====================================================================================================================

# nested loop in List Comprehension
n=int(input())
li=[((i+j)*10) for i in range(1,n+1)  for j in range(1,n+1)]
print(li)

=====================================================================================================================

# tuple() --> tuples are immutable
tup = tuple() # Constructor
tup = (29, 'python', 96.8)
print(tup)
a, b, c=tup # unpacking of tuples into variable
print(a, b, c)
# builtin fn of tuples
.count(), .index(), max(tuple), min(tuple), sum(tuple), len(tuple)

=====================================================================================================================

# Set()-> It is Unordered and cant be accessed by index value as it is not stored in the contiguous manner
'''Set is an unordered collection of values separated by commas and enclosed in {}
Set does not contain any duplicate value, set is mutable and frozen set is immutable.
set is not subscriptable.'''

s= set()
print(s,type(s))

s={}
print(s,type(s))

s={100,200,"hai",True,1,0,False,100,20,"Hello"}
print(s,type(s))

----------------------------------------------------------

'''set methods'''
s={100,200,"hai",True,1,0,False,100,20,"Hello"}

s.add(100)
print(s)
s.add(50)
print(s)
s.add(10)
print(s)
s.update("hai","hello")
s.update(["good","Hope"])
print(s)
s.remove(200) # removes the Item ,if the value is not found gives the error
s.discard(200) # if value not found then Does not gives the error

----------------------------------------------------------

[15:42, 02/01/2024] Pratik Patil PU: '''copy()'''
x={11,22,33,44}
y=x.copy()
print(x)
print(y)
'''clear()'''
y.clear() # Only clears the items but the object is still alive
print(y)
del y # this means the object or the Variable is also removed from the memory.

'''difference() & difference_update() --> it'll update the var/obj after difference'''

x={11,22,33,44}
y={1,2,3,45,6}
print("Difference x-y : ",x.difference(y) )
print("Difference x-y :",x.difference(y) )
x.difference_update(y)
print(x)

=====================================================================================================================

# Union of sets
lib1 = set(['apple', 'banana'])
lib2 = set(['guava', 'strawberyy'])
lib3 = lib1 | lib2
lib3 = lib1.union(lib2)
print(lib3)

# Symmetric Difference
lib3 = lib1 ^ lib2
print(lib3) # will remove simlilar ele
# difference
lib3 = lib1 - lib2 # will subtract lib2 elements from ib1 if present

# issubset and issuperset

lib1=set(["Numpy","teli"])
lib2=set(["pandas","Numpy"])
lib3=set(["pandas"])
issubset=lib1<=lib2
print(issubset)

issuperset=lib1>=lib2
print(issuperset)
issubset=lib3<=lib2
print(issubset)
issuperset=lib2>=lib3
print(issuperset)

# isdisjoint() and difference()
x=frozenset([1,2,3,4,5])
y=frozenset([3,4,5,6,7])

print(x.isdisjoint(y))  # return true if the set has no  element in common
print(x.difference(y)) #

# Set comprehension

square={i*i for i in range(1,6)}
print(square)


# Same program by set

square =set()
for i in range(1,6):
    square.add(i*i)
print(square)

=====================================================================================================================

# Dictionaries
parul={1: "CSE", (2,): "IT", 'Mech': 10, 'CIVIL':20}
print(parul)
parul[5]='Aviation' # dict[<key>]=<value>
print(parul)
print(parul.keys()) # will print keys
print(*parul.keys())
print(parul.values()) # will print values
print(*parul.values())
print(parul.items()) # will print items of the dict
print(*parul.items())
for k,v in parul.items():
    print(f"{k} --> {v}")

-------------------------------------------------------------------------------    

# heapq package
parul={10: 'Ten', 100: 'Hundred',1000:'Thousand'}
import heapq
print(heapq.nlargest(2,parul))
print(heapq.nsmallest(2,parul))

--------------------------------------------------------------------------------

# Dynamic input to dictionary
student={}
n=int(input("enter no. of students: "))
for i in range(n):
    rollNo = int(input())
    name = input()
    student[rollNo]=name
    #or
    # student.update({rollNo : name})
print(student)  

=====================================================================================================================

### Python Object Oriented Programming ###

'''Classes and Objects : '''


Classes and Objects are the fundamental components of OOPs
A class is a prototype that defines the variable and the functinos(methods) common  to all objects.
variables(characteristics/attributes) and functionalities (actions they perform ) defined inside the class are accessed through Objects.

EG:
class -> Email
Data Members -> properties
Methods -> (actions) - sending email,receiving email,adding attachments.
Objects are Instantiation of the Class
class in python is defined using the class keyword ,followed by the class name.
Syntax : class className(object):
            ..............Statement


from IPython.display import Image
Image(filename = "C:\Users\PratikPatil\OneDrive\Desktop\amazon-png-logo-vector-1.png",width=1000,height=1000)

---------------------------------------------------------------

#EG :

class Email:
    recipient="tana@gmail.com" 
    subject_line="Invitation"

    def sending(self):
        print("Email sent Successfully ")
     
    def attachment(self):
        print("File attached Successfully ")   
Email.sending(0)
Email.attachment(1)
print(Email.recipient)
print(Email.subject_line)


"""

